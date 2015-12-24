import movies
import fresh_tomatoes


toy_story = movies.Movie("Toy Story",
                        "Moving Toys",
                        "http://static.omelete.uol.com.br/media/extras/conteudos/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                        "https://pt.wikipedia.org/wiki/Toy_Story")



avatar = movies.Movie("Avatar",
                        "Pocahontas with aliens and 3D",
                        "https://screencraft.org/wp-content/uploads/2015/10/avatar.jpg",
                        "https://pt.wikipedia.org/wiki/Avatar")

movies = [toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)
#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()

