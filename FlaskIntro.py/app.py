#1 Create Flask App
from flask import Flask, render_template

app = Flask(__name__)

class Movie:
    def __init__(self, t, c, tu):
        self.title = t
        self.casts = c
        self.thumbnail_url = tu

m = Movie("Phineas and Ferb",
"Phineas, Ferb, Canadace",
  "https://www.wikihow.com/images/thumb/1/12/Draw-Phineas-Flynn-from-Phineas-and-Ferb-Step-20.jpg/aid1550346-v4-728px-Draw-Phineas-Flynn-from-Phineas-and-Ferb-Step-20.jpg")

m2 = Movie("Ant Man",
"Scott Lang, Hank Pym",
"http://image.phimmoi.net/film/2204/poster.medium.jpg ")

m3 = Movie("The Flash",
"Greg Berlanti, Andrew Kreisgberg",
"http://cdn1us.denofgeek.com/sites/denofgeekus/files/styles/main_wide/public/2018/05/the-flash-season-5-release-date-news-villain-story.jpg?itok=kLj80zyQ")


movie_list = [m, m2, m3]

@app.route("/")
def index():
    return render_template("index.html", name="Hoa", 
    image_url="https://i.pinimg.com/564x/d1/54/cc/d154cca7aeb121d0b9bb07306af4d9f8.jpg")

@app.route("/casts")
def casts():
    return render_template("casts.html", casts=["Phineas","Ferb","Canadace"])

@app.route("/movie")
def movie():
    return render_template("movie.html",movies = movie_list)

@app.route("/about-me")
def about_me():
    return "My name is Nhi. I'm in grade 12th. A true bookworm."

@app.route("/hello/<name>")
def hello(name):
    return "Hello " + name + " :>"

#2 Run app
if __name__ == "__main__":
    app.run(debug=True)