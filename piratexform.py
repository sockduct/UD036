# Imports
#import requests
# requests is better but use urllib for this since part of standard library
import urllib

# Variables
# File to check
targetfile = 'C:\Users\js646y\Documents\Projects-NB\Udacity\UD036\Programs\Provided\example_text.txt'
# Pirate translation web site
piratesite = 'http://isithackday.com/arrpi.php?text='

def readtext():
    quotes = open(targetfile)
    filecontents = quotes.read()
    print(filecontents)
    quotes.close()
    piratexlate(filecontents)

def piratexlate(targetstr):
    xlatecon = urllib.urlopen(piratesite + targetstr)
    xlateout = xlatecon.read()
    print(xlateout)
    xlatecon.close()

# Main
readtext()
