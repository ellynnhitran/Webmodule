from flask import *
import mlab
from models.movie import Movie

app = Flask(__name__)
app.config["SECRET_KEY"] = "hulu walmart # 9 XBOX FRUIT / @ YELP music + * fruit APPLE korean ZIP # NUT / XBOX VISA . music hulu DRIP YELP + @ EGG EGG 7 jack 4 ^ skype GOLF KOREAN VISA ! NUT ZIP egg 7 WALMART MUSIC"

mlab.connect()

@app.route("/")
def index():
  if "username" in session:
    movie_list = Movie.objects()
    return render_template("index.html", movies=movie_list)
  else:
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST":
    form = request.form
    username = form["username"]
    password = form["password"]
    if username == "admin" and password == "123456":
      #Valid credentials
      session["username"] = username
      return redirect("/")
    else:
      #Login fails
      flash("Login failed, username or password is incorrect")
      flash("Try again")
      return render_template("login.html")
 

if __name__ == "__main__":
  app.run(debug=True)