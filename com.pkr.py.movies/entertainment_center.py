import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print(toy_story.storyline)
# toy_story.show_trailer()

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

# print(avatar.storyline)
# avatar.show_trailer()

batman_vs_superman = media.Movie("Batman v Superman: Dawn of Justice",
                                 "Fearing the actions of a god-like super hero left unchecked, Gotham City’s own formidable, forceful vigilante takes on Metropolis’s most revered, modern-day savior, while the world wrestles with what sort of hero it really needs. And with Batman and Superman at war with one another, a new threat quickly arises, putting mankind in greater danger than it’s ever known before.",
                                 "https://en.wikipedia.org/wiki/File:Batman_v_Superman_poster.jpg",
                                 "https://www.youtube.com/watch?v=U652-BpXVQY")

# batman_vs_superman.show_trailer()

movies = [toy_story, avatar, batman_vs_superman]

# print(media.Movie.VALID_RATINGS)
# fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)