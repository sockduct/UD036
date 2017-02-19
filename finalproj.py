###########################################################################
# 
# Author:       James R. Small (js646y@att.com)
# Version:      1.0
# Since:        2015-10-09
# Last Update:  2015-10-25
#
# Description:  Programming Foundations Final Project
# Module:  Main program
#
###########################################################################
#
# Imports
# Python Standard Library
import os
import re
import sys
import webbrowser
# External Libraries
import bs4
import requests
# Import HockeyTeam Class
from hockeyteam import HockeyTeam

# Team HTML status page - head part
team_head_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Hockey Team Status Page</title>
    <style>
        table, th, td {
            border: 1px solid black;
            <!-- I am an HTML Comment -->
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
        }
        th {
            text-align: center;
        }
        td {
            text-align: center;
        }
        tr#titleCell {
            background-color: CadetBlue;
        }
        tr#grayCell {
            background-color: LightGray;
        }
        tr#plumCell {
            background-color: Plum;
        }
        tr#whiteCell {
            background-color: White;
        }
    </style>
</head>
  <body>
'''
# Team HTML status page - close out body part
body_close_page = '''
  </body>
</html>
'''

# Global Variables used as Constants
TIMEOUT = 10
# Windows 7 User Agent with Chrome
USERAGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
HOCKEYURI = 'http://'
HOCKEYSITE = 'www.pointstreak.com'
BASEPATH = '/players/'
TEAMPATH = 'players-team.html?teamid='
SEEDTEAMID = 514568

####################################################################################################
# Retrieve Passed Web Page (and deal with common problems) using requests
####################################################################################################
# For environments using a proxy:
#     HTTP_PROXY=http://19.12.1.140:83
#     HTTPS_PROXY=http://19.12.1.140:83
# Note:  Authentication is not accounted for in this example
####################################################################################################
#
# @param headers Headers to use within HTTP for web request
# @param url Site, path and file to attempt to retrieve
#
def getpage(headers,url):
    '''retrieve web page from <url> using <headers>'''
    session = requests.Session()
    try:
        print "Retrieving data from " + url + '...'
        resp = session.get(url,headers=headers,timeout=TIMEOUT)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print 'Client request or Server response error:\n' + str(error)
        sys.exit(-1)
    except requests.exceptions.ConnectionError as error:
        print 'Connection error:\n' + str(error)
        sys.exit(-2)
    except requests.exceptions.ReadTimeout as error:
        print 'Timeout waiting for server response:\n' + str(error)
        sys.exit(-3)
    except KeyboardInterrupt as error:
        print 'Detected keyboard interrupt, aborting...\n' + str(error)
        sys.exit(-4)
    #
    return resp

####################################################################################################
# Scrape team home page (retrieve with getpage above, parse with beautiful soup
####################################################################################################
#
# @param headers Headers to use within HTTP for web request
# @param url Site, path and file to attempt to retrieve
# @param team HockeyTeam class object used to store team information
#
def scrapeteamhome(headers,url,team):
    '''scrape relevant information from team home page (url) and put it in <team> class object'''
    resp = getpage(headers,url)
    respsoup = bs4.BeautifulSoup(resp.text,'html.parser')
    #
    # Scrape seasonid
    data = respsoup.find('td',{'class':'sideMenuHighlight'}).a
    data = re.findall(r'seasonid=[0-9]+',str(data))
    data = data[0]
    seasonid = int(data.strip('seasonid='))
    #
    # Scrape team schedule URL
    data = respsoup.findAll('td',{'class':'sideMenu'})
    for line in data:
        linestr = str(line)
        # Extract team schedule page
        if re.search(r'players-team-schedule',linestr):
            teamsched = re.findall(r'a href="[^"]*"',linestr)[0]
            teamsched = teamsched.split('href=')[1][1:-1]
        # Extract team division standings page and divisionid
        if re.search(r'players-division-standings',linestr):
            divstand = re.findall(r'a href="[^"]*"',linestr)[0]
            divstand = divstand.split('href=')[1][1:-1]
            divisionid = int(re.findall(r'divisionid=[0-9]+',divstand)[0].strip('divisionid='))
        # Extract team division schedule page
        if re.search(r'players-division-schedule',linestr):
            divsched = re.findall(r'a href="[^"]*"',linestr)[0]
            divsched = divsched.split('href=')[1][1:-1]
    team.newseason('Fall/Winter 2015/2016',seasonid,'Pee Wee A','Howe 2','Blue',divisionid, \
        url,teamsched,divstand,divsched,True)

####################################################################################################
# Scrape team division standings page
####################################################################################################
#
# @param headers Headers to use within HTTP for web request
# @param url Site, path and file to attempt to retrieve
# @param team HockeyTeam class object used to store team information
#
def scrapeteamdivstand(headers,url,team):
    '''scrape relevant information from team division standings page (url) and put it in <team>
    class object'''
    resp = getpage(headers,url)
    respsoup = bs4.BeautifulSoup(resp.text,'html.parser')
    #
    # Use this sequence to find all teams in the division group
    teamre = r'players-team\.html\?teamid='
    dteams = respsoup.findAll('a',{'href':re.compile(teamre)})
    divisionteams = []
    # Iterate through each team in the division group
    for dteam in dteams:
        # Parse out relevant information for each division team
        divisionteamid = int(re.findall(r'teamid=[0-9]+',str(dteam))[0].strip('teamid='))
        divisionteamname = dteam.get_text().strip().encode('ascii')
        divisionteams.append({'name':divisionteamname,'teamid':divisionteamid})
        teamidre = teamre + str(divisionteamid)
        teamrecord = {'divteamname':divisionteamname,'divteamid':divisionteamid,'divteamstats':None}
        teamstats = []
        # Starting from a specific element for the division team in question, collect all elements
        # from the row (siblings) and iterate through them.  Only elements within HTML tags are
        # of interest, skip everything else.  We also change from Unicode encoding to ASCII.  If
        # this were in Python 3.x, this decision should be re-visited.
        for sibling in \
                respsoup.find('a',{'href':re.compile(teamidre)}).parent.parent.td.next_siblings:
            if isinstance(sibling,bs4.element.Tag):
                teamstats.append(sibling.get_text().encode('ascii'))
        teamrecord['divteamstats'] = teamstats[:]
        team.updateteamstanding(teamrecord)

####################################################################################################
# Scrape team schedule page
####################################################################################################
#
# @param headers Headers to use within HTTP for web request
# @param url Site, path and file to attempt to retrieve
# @param team HockeyTeam class object used to store team information
#
def scrapeteamsched(headers,url,team):
    '''scrape relevant information from team schedule page (url) and put it in <team>
    class object'''
    resp = getpage(headers,url)
    respsoup = bs4.BeautifulSoup(resp.text,'html.parser')
    #
    pagedata = respsoup.find('tr',{'class':'fields'}).parent
    # Starting from the top of the table with the team schedule information, iterate through
    # each row.  As with above, we're only interested in elements within HTML tags.
    for child in pagedata.children:
        if isinstance(child,bs4.element.Tag):
            teamschedmatrix = []
            datagroup = child.descendants
            # Iterate through elements of each row, only interested in what beautiful soup
            # calls "NavigableSring".  If the string only consists of white space (length < 1)
            # then we skip it.
            for datum in datagroup:
                if isinstance(datum,bs4.element.NavigableString):
                    output = datum.strip()
                    if len(output) >= 1:
                        teamschedmatrix.append(output.encode('ascii'))
            team.updateteamschedule(teamschedmatrix)

####################################################################################################
# Create team status page (HTML)
####################################################################################################
#
# @param team HockeyTeam class object used to store team information
#
def createteampage(team):
    '''generate HTML page with team division standings, game record and future schedule using
    information from <team> class object'''
    # Create web page content
    content = ''
    content += '<h1>' + team.league + '</h1>'
    content += '<h2>' + team.leaguetype + ', ' + team.season + ', ' + team.agegroup + '</h2>'
    ################################################################################
    # Create team division status page
    ################################################################################
    content += '<h3>Division Standings for ' + team.ldivision + ' - ' + team.ldivisiongroup + '</h3>'
    content += '<table style="width:60%">'
    content += '<tr id="titleCell"><th>Team</th> <th>GP</th> <th>Win</th> <th>Loss</th> <th>Tie</th>'
    content += '<th>Pts</th> <th>GF</th> <th>GA</th> <th>PM</th> <th>Last 5</th> <th>Streak</th><tr>'
    # Go through record for each team in division
    for dteamnum,dteamrec in enumerate(team.divteamrecords):
        # Color code alternate rows to make viewing data easier, special color for this team
        if dteamrec['divteamname'] == 'Jimmy Johns - Cranbrook 04':
            content += '<tr id="plumCell">'
        elif dteamnum % 2 == 0:
            content += '<tr id="whiteCell">'
        else:
            content += '<tr id="grayCell">'
        content += '<td align="left">' + dteamrec['divteamname'] + '</td>'
        # Put each team statistic in a separate column
        for dteamstat in dteamrec['divteamstats']:
            content += '<td>' + dteamstat + '</td>'
        content += '</tr>'
    content += '</table>'
    ################################################################################
    # Create team schedule page (Game Record for past, Game Schedule for future)
    ################################################################################
    content += '<h3>' + team.name + ' Game Record</h3>'
    content += '<table style="width:80%">'
    content += '<tr id="titleCell"><th>Game #</th> <th>Result</th> <th>Home</th> <th>GF</th>'
    content += '<th>Away</th> <th>GA</th> <th>Date</th> <th>Time</th>'
    content += '<th>Rink/GS</th> <tr>'
    titleflag = True
    lentsm = len(team.teamschedmatrix)
    # Go through each record in team schedule
    for lnum,line in enumerate(team.teamschedmatrix):
        lenline = len(line)
        # Skip first line (printed title row above)
        if lnum == 0:
            pass
        # Skip last line (extraneous info)
        elif lnum == lentsm - 1:
            pass
        # If the last column is marked 'final' it means the game was already played
        # and the score has been entered
        elif line[lenline-1] == 'final':
            #print 'Played:  ' + str(line)
            if lnum % 2 == 0:
                content += '<tr id="grayCell">'
            else:
                content += '<tr id="whiteCell">'
            # Determine result of game (win/loss/tie)
            score = int(line[2]) - int(line[4])
            if score > 0:
                result = 'Win'
            elif score == 0:
                result = 'Tie'
            else:
                result = 'Loss'
            for enum,elmt in enumerate(line):
                # Add game result in
                if enum == 1:
                    content += '<td>' + result + '</td>'
                content += '<td>' + elmt + '</td>'
            content += '</tr>'
        # If the last column is marked 'data pending' it means the game was already
        # played, but the score has not been entered yet
        elif line[lenline-1] == 'data pending':
            #print 'Pending:  ' + str(line)
            # Color code alternate rows to make viewing data easier
            if lnum % 2 == 0:
                content += '<tr id="grayCell">'
            else:
                content += '<tr id="whiteCell">'
            # Put each element in a separate column
            for enum,elmt in enumerate(line):
                # Since the score hasn't been entered yet, we have to enter
                # 'pending' for the result and where the score should be
                if enum == 1 or enum == 2 or enum == 3:
                    content += '<td>pending</td>'
                content += '<td>' + elmt + '</td>'
            content += '</tr>'
        # Everything else is a future (scheduled) game
        else:
            # Put future game schedule in a separate table
            if titleflag:
                titleflag = False
                content += '</table>'
                content += '<h3>' + team.name + ' Upcoming Games</h3>'
                content += '<table style="width:70%">'
                content += '<tr id="titleCell"><th>Game #</th> <th>Home</th> <th>Away</th>'
                content += '<th>Date</th> <th>Time</th> <th>Rink/GS</th> <tr>'
            #print 'Scheduled:  ' + str(line)
            # Color code alternate rows to make viewing data easier
            if lnum % 2 == 0:
                content += '<tr id="grayCell">'
            else:
                content += '<tr id="whiteCell">'
            # Put each element in a separate column
            for enum,elmt in enumerate(line):
                content += '<td>' + elmt + '</td>'
            content += '</tr>'
    content += '</table>'
    #
    return content

####################################################################################################
# Main Procedure
####################################################################################################
if __name__ == '__main__':
    mysonsteam = HockeyTeam('Jimmy Johns Hockey Club 04',SEEDTEAMID, \
        "Little Caesar's Amateur Hockey League",'Travel')
    #
    ################################################################################
    # Scrape data from team home page
    ################################################################################
    headers = {'User-Agent':USERAGENT,'Accept':ACCEPT}
    url = HOCKEYURI+HOCKEYSITE+BASEPATH+TEAMPATH+str(SEEDTEAMID)
    scrapeteamhome(headers,url,mysonsteam)
    #
    ################################################################################
    # Scrape data from team division standings page
    ################################################################################
    headers = {'User-Agent':USERAGENT,'Accept':ACCEPT}
    url = HOCKEYURI+HOCKEYSITE+BASEPATH+mysonsteam.divstandpath
    scrapeteamdivstand(headers,url,mysonsteam)
    #
    ################################################################################
    # Get data from team schedule page
    ################################################################################
    headers = {'User-Agent':USERAGENT,'Accept':ACCEPT}
    url = HOCKEYURI+HOCKEYSITE+BASEPATH+mysonsteam.teamschedpath
    scrapeteamsched(headers,url,mysonsteam)
    #
    ################################################################################
    # Create team status page and open in default browser
    ################################################################################
    # Create/overwrite output file
    outputfile  = open('teamstatspage.html','w')
    content = createteampage(mysonsteam)
    outputfile.write(team_head_page + content + body_close_page)
    outputfile.close()
    #
    teamstatspage = os.path.abspath(outputfile.name)
    webbrowser.open('file://' + teamstatspage,new=2)

