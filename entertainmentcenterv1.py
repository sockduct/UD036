# File 2 - entertainmentcenter.py
# Good best practice to define class(es) in a separate file
# and import them where it/they is/are used

# Imports
# Import my media.py file contents
import media

# Toy Story Official Trailer #1 YouTube code:  KYz2wyBy3kc
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
#print(media.Movie(toy_story.storyline))
#print(toy_story.movietype)
#toy_story.movietype = 'my favorites'
#print(toy_story.movietype)

# Avatar Official Trailer YouTube code:  5PSNL1qE6VY
# Class YouTube code (marked as private):  -9ceBgWV8io
avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock", "Storyline",
                    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "Storyline",
                    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                    "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games", "Storyline",
                    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                    "https://www.youtube.com/watch?v=PbA63a7H0bo")

#print(avatar.storyline)
#print(avatar.movietype)
#avatar.showimage()
#avatar.showtrailer()

#hpotterdh1 = media.Movie("Harry Potter and the Deathly Hallows, Part 1",
#                    "A young wizard's quest to destroy his diabolical nemesis",
#                    "https://upload.wikimedia.org/wikipedia/en/2/2d/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_1.jpg",
#                    "http://www.youtube.com/watch?v=MxqsmsA8y5k")
#
#print(hpotterdh1.storyline)
#hpotterdh1.showimage()
#hpotterdh1.showtrailer()
#print(media.Movie.VALID_RATINGS)
#
# Pre-defined Class Attributes
print media.Movie.__dict__
print media.Movie.__name__
print media.Movie.__bases__
print media.Movie.__doc__
print media.Movie.__module__
#
# Pre-defined Instance Attributes
print avatar.__dict__
print avatar.__class__
