###########################################################################
# 
# Author:       James R. Small (js646y@att.com)
# Version:      1.0
# Since:        2015-10-09
# Last Update:  2015-10-25
#
# Description:  Programming Foundations Final Project
# Module:  Class definition for Youth Hockey Team
#
###########################################################################


####################################################################################################
# Use new-style classes
# Details:  https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html
# Note:  In Python 3, new-style classes are the default
#        Old-style classes are only available in Python 2
#        Consensus seems to be to only use the new style classes and avoid the old style.
####################################################################################################
class HockeyTeam(object):
    '''store relevant data for a youth league hockey team'''
    def __init__(self,name,uid,league,leaguetype):
        '''initialize team with minimum information'''
        self.name = name
        self.uid = uid
        self.league = league
        self.leaguetype = leaguetype
        self.season = None
        self.sid = 0
        self.agegroup = None
        self.ldivision = None
        self.ldivisiongroup = None
        self.gid = 0
        self.teamsite = None
        self.teamschedpath = None
        self.divstandpath = None
        self.divschedpath = None
        self.xover = False
        self.divteamrecords = []
        self.teamschedmatrix = []

    def __repr__(self):
        print '------------------------------------------------------------------------'
        print 'Team Name:  ' + self.name
        print 'Team Unique ID:  ' + str(self.uid)
        print 'League:  ' + self.league
        print 'League Type:  ' + self.leaguetype
        print '------------------------------------------------------------------------'
        print 'Season:  ' + self.season
        print 'Season ID:  ' + str(self.sid)
        print 'Team Age Group:  ' + self.agegroup
        print 'League Division:  ' + self.ldivision
        print 'League Division Group:  ' + self.ldivisiongroup
        print 'Division Group ID:  ' + str(self.gid)
        print 'Team Home Page:  ' + self.teamsite
        print 'Team Schedule Page:  ' + self.teamschedpath
        print 'Division Standings Page for Team:  ' + self.divstandpath
        print 'Division Schedule Page for Team:  ' + self.divschedpath
        print 'Crossover Division?  ' + str(self.xover)
        print '------------------------------------------------------------------------'
        print 'Division Teams and Team Statistics:'
        print '(GP, W, L, T, PTS, GF, GA, PIM, Last5, Streak)'
        for team in self.divteamrecords:
            print team['divteamname'] + ' - ' + str(team['divteamid']) + ':'
            print team['divteamstats']
        print '------------------------------------------------------------------------'
        print self.name + ' Team Schedule:'
        lentsm = len(self.teamschedmatrix)
        for lnum,line in enumerate(self.teamschedmatrix):
            lenline = len(line)
            if lnum == 0:
                print '(' + str(line) + ')'
            elif lnum == lentsm - 1:
                # Skip last line
                pass
            elif line[lenline-1] == 'final':
                print 'Played:  ' + str(line)
            elif line[lenline-1] == 'data pending':
                print 'Pending:  ' + str(line)
            else:
                print 'Scheduled:  ' + str(line)
        #print '------------------------------------------------------------------------'
        # Don't return object dictionary, but must return string or get an error
        #print 'Object dictionary:'
        #return str(self.__dict__)
        return '------------------------------------------------------------------------'

    def newseason(self,season,sid,agegroup,ldivision,ldivisiongroup,gid,teamsite,teamschedpath, \
            divstandpath,divschedpath,xover=False):
        '''initialize team to start new season'''
        self.season = season
        self.sid = sid  # Season ID
        self.agegroup = agegroup
        self.ldivision = ldivision
        self.ldivisiongroup = ldivisiongroup
        self.gid = gid  # Division Group ID
        self.teamsite = teamsite  # URL
        self.teamschedpath = teamschedpath  # Relative path
        self.divstandpath = divstandpath  # Relative path
        self.divschedpath = divschedpath  # Relative path
        self.xover = xover  # Default is group is not part of crossover group

    def xoverseason(self,xovergroup,xovergid):
        '''initialize team to participate in crossover games for season'''
        self.xover = True  # If invoke this method, must be a crossover group
        self.xovergroup = xovergroup
        self.xovergid = xovergid

    def updateteamstanding(self,divteamrecords):
        '''update team's division standing statistics from master web site'''
        # TeamRecord:
        # TeamName, TeamID, GP, W, L, T, PTS, GF, GA, PIM, Last5, Streak
        self.divteamrecords.append(divteamrecords)

    def updateteamschedule(self,teamschedmatrix):
        '''update team's future schedule from master web site'''
        # Update team's future schedule
        # Game number, Home Team, Away Team, Date, Time, Rink/GS (Game Status), GT
        # If date/time in the past then two options:
        # 1) GS = final, home/away team will be followed by respective score
        # 2) GS = data pending, scores not entered yet
        # Look at score and determine if Win/Loss/Tie
        # If data/time in future then it's upcoming schedule and Rinks/GS column
        # will be the planned game location (rink)
        self.teamschedmatrix.append(teamschedmatrix)

