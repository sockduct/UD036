# Imports
import os
import random

# Variables
# For Windows use a raw string since backslashes are used
dirpath = r'C:\Users\js646y\Documents\Projects-NB\Udacity\UD036\Programs\Provided\Message'

# Randomize files using string translation
def scramblefiles():
    count = 0
    dirfiles = os.listdir(dirpath)
    savedir = os.getcwd()
    os.chdir(dirpath)
    for dirfile in dirfiles:
        nextnum = random.randint(0,99)
        # Make sure number string is two digits by prepending a zero if necessary
        numstr = str(nextnum).zfill(2)
        newfile = numstr + dirfile
        print("Old filename:  " + dirfile)
        print("New filename:  " + newfile)
        os.rename(dirfile,newfile)
        count +=1
    os.chdir(savedir)
    print("\nRenamed " + str(count) + " files.\n")

scramblefiles()

