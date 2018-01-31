import media
import fresh_tomatoes 

toy_story = media.Movie("Toy Story",
                                                "storyline story line, this is storyline",
                                                "http://www.cultjer.com/img/ug_photo/2015_09/32772420150915154419.jpg",
                                                "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                                   "storyline of avatar movie",
                                    "https://s3.amazonaws.com/udacity-hosted-downloads/ud036/Creating+the+instance+avatar.png",
                                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")

everest = media.Movie("Everest",
                                          "storyline of Everest",
                                          "http://www.kino-sokol.pl/media/Movies/poster_608.jpg",
                                          "https://www.youtube.com/watch?v=dOHS-mxn0RQ")

great_silence = media.Movie("Into Great Silence",
                                   "storyline of avatar movie",
                                    "https://images-na.ssl-images-amazon.com/images/I/41gRZJIl5RL._SY445_.jpg",
                                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")

space_odyssey2001 = media.Movie("Space Odyssey 2001",
                                          "storyline of Everest",
                                          "https://cdn1.pamono.com/p/z/2/1/219481_s29tcjivfq/2001-a-space-odyssey-film-poster-1968-1.jpg",
                                          "https://www.youtube.com/watch?v=dOHS-mxn0RQ")

one_six_right = media.Movie("One Six Right",
                                   "storyline of avatar movie",
                                    "https://upload.wikimedia.org/wikipedia/en/9/98/OneSixRight_poster_medium.jpg",
                                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")

footprints = media.Movie("Footprints - path of your life",
                                          "storyline of Everest",
                                          "https://images-na.ssl-images-amazon.com/images/M/MV5BZTVlNjFlNDItYzNiMy00NmUxLWExZTgtYjBkMWI4YjQ4YzQ4XkEyXkFqcGdeQXVyNjMyMDIxMjE@._V1_UY1200_CR113,0,630,1200_AL_.jpg",
                                          "https://www.youtube.com/watch?v=dOHS-mxn0RQ")

#print(avatar.storyline)
                   
#avatar.show_trailer()
#toy_story.show_trailer()
#everest.show_trailer()
movies = [toy_story, avatar, everest, great_silence, space_odyssey2001, one_six_right, footprints]

fresh_tomatoes.open_movies_page(movies)
