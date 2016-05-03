import webbrowser
class Movie():
    """This is a class to store movie information, such as the title,
    storyline description, movie poster, and the movie trailer."""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """When called, creates instances of Movie. Takes as arguments movie title,
        storyline, link to the movie's image, and a link to the youtube trailer."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """launches web browser to open movie trailer's youtube link"""
        webbrowser.open(self.trailer_youtube_url)
