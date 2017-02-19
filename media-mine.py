# File1 - media.py
# Good best practice to define class(es) in a separate file

# Imports
import webbrowser
import urllib2 as urllib
import io
from PIL import Image

class Movie():
    movietype = 'favorites'

    def __init__(self,movietitle,moviestoryline,posterimage,traileryoutube):
        self.title = movietitle
        self.storyline = moviestoryline
        # This changes storyline from an instance variable to a local variable
        # Trying to access it outside of this function will result in an error
        # because it doesn't exist (only exists in local scope)
        #storyline = moviestoryline
        self.posterimageurl = posterimage
        self.traileryoutubeurl = traileryoutube

    def showimage(self):
        movieimagefd = urllib.urlopen(self.posterimageurl)
        movieimageio = io.BytesIO(movieimagefd.read())
        movieimage = Image.open(movieimageio)
        movieimage.show()

    def showtrailer(self):
        webbrowser.open(self.traileryoutubeurl)

