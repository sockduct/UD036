# Imports
import os
import re

# Variables
# For Windows use a raw string since backslashes are used
dirpath = r'C:\Users\js646y\Documents\Projects-NB\Udacity\UD036\Programs\Provided\prank'

# Rename files use regexp
def renamefilesre():
    dirfiles = os.listdir(dirpath)
    for dirfile in dirfiles:
        newfile = re.findall(r'\D',dirfile)
        newfile = ''.join(newfile)
        #os.rename(dirfile,newfile)
        print "Old filename:  " + str(dirfile)
        print "New filename:  " + str(newfile)

# Rename files using string translation
def renamefilesst():
    count = 0
    dirfiles = os.listdir(dirpath)
    savedir = os.getcwd()
    os.chdir(dirpath)
    for dirfile in dirfiles:
        newfile = dirfile.translate(None,"0123456789")
        print("Old filename:  " + dirfile)
        print("New filename:  " + newfile)
        os.rename(dirfile,newfile)
        count +=1
    os.chdir(savedir)
    print("\nRenamed " + str(count) + " files.\n")

#renamefilesre()
renamefilesst()

