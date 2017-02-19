# Imports
import bs4
import re
import requests
import sys
# Import HockeyTeam Class
from hockeyteam import HockeyTeam

# Variables
TIMEOUT = 10
# iPhone User Agent with Safari
#USERAGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53'
# Windows 7 User Agent with Chrome
USERAGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
hockeyuri = 'http://'
hockeysite = 'www.pointstreak.com'
basepath = '/players/'
teampath = 'players-team.html?teamid='
# Either pre-populate or create way to search for it
teamid = 514568
#hockeypath = '/players/players-division-standings.html'
#divisionid = '79195'
#seasonid = '14710'
#testurl = 'http://httpbin.org/status/403'

# Retrieve Web Page
####################################################################################################
#
# Note:  Easiest way to use proxies is with environment variables:
#           HTTP_PROXY=http://19.12.1.140:83
#           HTTPS_PROXY=http://19.12.1.140:83
#
def getpage(headers,url):
    '''retrieve web page from <url> using <headers>'''
    session = requests.Session()
    try:
        print "Connecting to " + url + '...'
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

# Scrape team home page
####################################################################################################
def scrapeteamhome(headers,url):
    resp = getpage(headers,url)
    respsoup = bs4.BeautifulSoup(resp.text,'html.parser')
    #
    # Need to use try/except for bs4 operations:
    # try:
    #   badcontent = respsoup.h1.dne.h2
    #   (can do multiple/all bs4 ops in one try)
    # except AttributeError as error:
    #   print 'Tag not found:\n' + str(error)
    # else:
    #   if badcontent == None:
    #     print 'Tag not found!'
    #   else:
    #     print(badcontent)
    #
    # Scrape seasonid
    data = respsoup.find('td',{'class':'sideMenuHighlight'}).a
    data = re.findall(r'seasonid=[0-9]+',str(data))
    data = data[0]
    seasonid = int(data.strip('seasonid='))
    print 'Season ID = ' + str(seasonid)
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
    print 'Team Schedule:  ' + str(teamsched)
    print 'Division Standings:  ' + str(divstand)
    print 'Division Schedule:  ' + str(divsched)
    print 'Division ID:  ' + str(divisionid)

# Scrape team division standings page
####################################################################################################
def scrapeteamdivstand(headers,url):
    resp = getpage(headers,url)
    respsoup = bs4.BeautifulSoup(resp.text,'html.parser')
    #
    teamre = r'players-team\.html\?teamid='
    teams = respsoup.findAll('a',{'href':re.compile(teamre)})
    divisionteams = []
    for team in teams:
        divisionteamid = int(re.findall(r'teamid=[0-9]+',str(team))[0].strip('teamid='))
        divisionteamname = team.get_text().strip()
        divisionteams.append({'name':divisionteamname,'teamid':divisionteamid})
        print divisionteamname + ' - ' + str(divisionteamid) + ':'
        teamidre = teamre + str(divisionteamid)
        for sibling in \
          respsoup.find('a',{'href':re.compile(teamidre)}).parent.parent.td.next_siblings:
            if isinstance(sibling,bs4.element.Tag):
                print sibling.get_text()

# Scrape team schedule page
####################################################################################################
def scrapeteamsched(headers,url):
    respsoup = bs4.BeautifulSoup(resp.text,'html.parser')
    #
    print 'Table:'
    pagedata = respsoup.find('tr',{'class':'fields'}).parent
    for child in pagedata.children:
        #print 'Child type:  ' + str(type(child))
        if isinstance(child,bs4.element.Tag):
            datagroup = child.descendants
            for datum in datagroup:
                if isinstance(datum,bs4.element.NavigableString):
                    output = datum.strip()
                    if len(output) >= 1:
                        print output

# Main
####################################################################################################
if __name__ == '__main__':
    ################################################################################
    # Scrape data from team home page
    ################################################################################
    headers = {'User-Agent':USERAGENT,'Accept':ACCEPT}
    url = hockeyuri+hockeysite+basepath+teampath+str(teamid)
    scrapeteamhome(headers,url)
    ################################################################################
    #
    ################################################################################
    # Scrape data from team division standings page
    ################################################################################
    headers = {'User-Agent':USERAGENT,'Accept':ACCEPT}
    url = hockeyuri+hockeysite+basepath+divstand
    scrapeteamdivstand(headers,url)
    ################################################################################
    # Get data from team schedule page
    ################################################################################
    headers = {'User-Agent':USERAGENT,'Accept':ACCEPT}
    url = hockeyuri+hockeysite+basepath+teamsched
    resp = getpage(headers,url)
    scrapeteamsched(headers,url)
    #elements = respsoup.findAll('tr',{'class':'lightGrey'})
    #for element in elements:
    #    for childelt in element.children:
    #        if isinstance(childelt,bs4.element.Tag):
    #            print childelt.get_text()
    #
    #
    #print respsoup.title
    #print respsoup.h1
    #print respsoup.h2
    #teams = respsoup.findAll('a',{'href':re.compile('players-team\.html\?teamid=')})
    #print 'Teams:\n'
    #for team in teams:
    #    print team
    #print '\nTeam ID 454751 stats:\n'
    #for sibling in respsoup.find('a',{'href':re.compile('players-team\.html\?teamid=454751')}).parent.parent.td.next_siblings:
    #    print sibling
    #
    #names = respsoup.findAll('td',{'class':'cellDivision'})
    #print respsoup.findAll('td',{'class':'cellDivision'})
    #print respsoup.findAll('tr',{'class':'fields'})
    #names = respsoup.findAll('tr',{'class':'fields'})
    #for name in names:
    #    print(name.get_text())
    #print 'Siblings:\n'
    #for sibling in respsoup.find('tr',{'class':'whiteCell'}).td.next_siblings:
    #    print(sibling)
    # Would like to combine in one operation but if use 'class' twice doesn't work:
    #names = respsoup.findAll('tr',{'class':'whiteCell','class':'lightGrey'})
    #print 'Team data:\n' #+ str(names)
    #for name in names:
    #    print(name.get_text())
    #names = respsoup.findAll('tr',{'class':'lightGrey'})
    #for name in names:
    #    print(name.get_text())
    #
    #print 'Siblings:\n'
    #siblings = respsoup.findAll('tr',{'class':'lightGrey'})
    #for sibling in siblings.td.next_siblings:
    #    print(sibling)
    #
    #print '\nRest:\n'
    #print respsoup
    #print respsoup.select('table h1')
    #print respsoup.select('table h2')
    #print respsoup.select('table tbody tr td')

