# File1 - media.py
# Good best practice to define class(es) in a separate file

# Imports
import webbrowser
import urllib2 as urllib
import io
from PIL import Image

class Movie():
    '''This class provides a way to store movie related information'''
    # The above is accessed for movie.Movie.__doc__
    movietype = 'favorites'
    # Per Google Style Guide, use All-Caps for constants
    VALID_RATINGS = ['G','PG','PG-13','R']

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        # This changes storyline from an instance variable to a local variable
        # Trying to access it outside of this function will result in an error
        # because it doesn't exist (only exists in local scope)
        #storyline = moviestoryline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showimage(self):
        movieimagefd = urllib.urlopen(self.poster_image_url)
        movieimageio = io.BytesIO(movieimagefd.read())
        movieimage = Image.open(movieimageio)
        movieimage.show()

    def showtrailer(self):
        webbrowser.open(self.trailer_youtube_url)

