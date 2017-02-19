# File 2 - entertainmentcenterv3.py
# Good best practice to define class(es) in a separate file
# and import them where it/they is/are used

# Imports
# Import my media.py file contents
import media
import fresh_tomatoes

# My 6 favorite movies
matrix = media.Movie("The Matrix",
                    "The protagonist's quest reveals that nothing is like it seems",
                    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

captainamer = media.Movie("Captain America, The First Avenger",
                    "A weak man is transformed into a selfless hero",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/" +
                        "Captain_America_The_First_Avenger_poster.jpg",
                    "https://www.youtube.com/watch?v=JerVrbLldXw")

avengersaou = media.Movie("Avengers: Age of Ultron",
                    "The Avengers unwittingly create their own nemesis",
                    "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                    "https://www.youtube.com/watch?v=hpazy0BHzxY")

hpotterdh1 = media.Movie("Harry Potter and the Deathly Hallows, Part 1",
                    "A young wizard's quest to destroy his diabolical nemesis",
                    "https://upload.wikimedia.org/wikipedia/en/2/2d/" +
                        "Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_1.jpg",
                    "http://www.youtube.com/watch?v=MxqsmsA8y5k")

startrekwok = media.Movie("Star Trek II: The Wrath of Khan",
                    "Captain Kirk unexpectedly clashes with a past arch-rival",
                    "http://www.standbyformindcontrol.com/wp-content/uploads/2013/05/khan-poster.jpg",
                    "https://www.youtube.com/watch?v=vOIYaRb6XpQ")

startrekins = media.Movie("Star Trek: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Insurrection",
                    "Captain Picard finds himself in the midst of a conspiracy",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/" +
                        "Star_Trek_Insurrection.png/220px-Star_Trek_Insurrection.png",
                    "https://www.youtube.com/watch?v=N1XmtdMZdL8")

movies = [hpotterdh1,startrekwok,startrekins,avengersaou,captainamer,matrix]
fresh_tomatoes.open_movies_page(movies)

