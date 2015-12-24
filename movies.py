"""
Movies project from udacity's python programming course
"""
import webbrowser
#Movie Class definition
class Movie():
    #__name__, __doc__, __module__
    """This class provides a way to store movie info """
    VALID_RATINGS = ["G", "PG", "XXX"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
        #'self' allows to make instance variables
        # without it, we get simple local variables
        

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


        
