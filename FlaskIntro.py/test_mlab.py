from mongoengine import *

class Movie(Document):
    title = StringField()
    image_url = StringField()
    link = StringField()

# 1 Connect to mlab
import mlab
mlab.connect()

# # # 2 Create a movie
# movie = Movie(title="Love, Rosie", image_url="https://i.ytimg.com/vi/C3m5w7iC4VM/maxresdefault.jpg", 
# link="https://i.ytimg.com/vi/C3m5w7iC4VM/maxresdefault.jpg")


# # # 3 Send newly created movie to mlab
# movie.save()

movie_list = Movie.objects() #lazy loading
for movie in movie_list:
    print(movie.title)
    print(movie.image_url)
    print(movie.link)
    print("**************")
