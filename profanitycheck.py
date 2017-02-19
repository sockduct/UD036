# Imports
#import requests
# requests is better but use urllib for this since part of standard library
import urllib

# Variables
# File to check
profanityfile = 'C:\Users\js646y\Documents\Projects-NB\Udacity\UD036\Programs\Provided\movie_quotes.txt'
#profanityfile = 'C:\Users\js646y\Documents\Projects-NB\Udacity\UD036\Programs\Provided\movie_quotes_exp.txt'
# Profanity checking web site
profanitysite = 'http://www.wdyl.com/profanity?q='

def readtext():
    quotes = open(profanityfile)
    filecontents = quotes.read()
    #print(filecontents)
    quotes.close()
    profanitycheck(filecontents)

def profanitycheck(chkstr):
    profcon = urllib.urlopen(profanitysite + chkstr)
    profout = profcon.read()
    #print(profout)
    profcon.close()
    if 'true' in profout:
        print('Profanity Alert!')
    elif 'false' in profout:
        print('This document contains no recognized curse words.')
    else:
        print('Error scanning the document.')

# Main
readtext()
