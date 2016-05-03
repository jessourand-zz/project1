import fresh_tomatoes
import media
import webbrowser

big_lebowski = media.Movie( "The Big Lebowski",
                            "The Dude abides.",
                            "http://cache.reelz.com/assets/content/article/lebowski-10th-cover.jpg",
                            "https://www.youtube.com/watch?v=cd-go0oBF4Y")

goodfellas = media.Movie(   "Goodfellas",
                            "The original story of a man doing hoodrat things with his hoodrat friends.",
                            "http://ecx.images-amazon.com/images/I/81NuuGhiNmL._SL1500_.jpg",
                            "https://www.youtube.com/watch?v=2ilzidi_J8Q")

dumb_dumber = media.Movie(  "Dumb and Dumber",
                            "The story of a dumb man's journey.",
                            "http://ia.media-imdb.com/images/M/MV5BMTIzNDI5MTc0M15BMl5BanBnXkFtZTYwMjM5NDU5._V1_SX640_SY720_.jpg",
                            "https://www.youtube.com/watch?v=T1uQZhQzQAI")

forrest_gump = media.Movie( "Forrest Gump",
                            "A slow-witted man's journey through life.",
                            "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                            "https://www.youtube.com/watch?v=bLvqoHBptjg")

zombieland = media.Movie(   "Zombieland",
                            "A zombie survival-guide featuring Bill Fuckin' Murray.",
                            "https://upload.wikimedia.org/wikipedia/en/a/a3/Zombieland-poster.jpg",
                            "https://www.youtube.com/watch?v=wSoWAE_KzBg")

monsters_inc = media.Movie( "Monsters, inc.",
                            "Corporate monsters make a living by scaring humans",
                            "http://vignette4.wikia.nocookie.net/disney-fan-fiction/images/0/04/MonstersIncposter.jpg/revision/latest?cb=20130724162723",
                            "https://www.youtube.com/watch?v=8IBNZ6O2kMk")

movies = [big_lebowski, dumb_dumber, forrest_gump, goodfellas, monsters_inc, zombieland]
fresh_tomatoes.open_movies_page(movies)
