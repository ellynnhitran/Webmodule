from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", name="Nhi", 
    image_url="https://i.pinimg.com/564x/d1/54/cc/d154cca7aeb121d0b9bb07306af4d9f8.jpg")

class Content:
    def __init__(self, l, c):
        self.link = l
        self.content = c

c1 = Content("https://www.newyorker.com/news", 
"News")
c2 = Content("https://www.newyorker.com/culture",
"Culture")
c3 = Content("https://www.newyorker.com/books",
"Books")
c4 = Content("https://www.newyorker.com/humor",
"Humor")
content_list = [c1, c2, c3, c4]

class Popular:
    def __init__(self, i, t, u, n, a):
        self.index = i
        self.title = t
        self.url = u
        self.name_url = n
        self.author = a

p1 = Popular("1.", "Letter from Washington", "https://www.newyorker.com/humor",
"The danger of president pence", "Jane Mayer")
p2 = Popular("2.", "Our Columnists", "https://www.newyorker.com/humor", 
"No End in Sight to the Brexit Madness", "John Cassidy")
p3 = Popular("3.", "Satire from the Borowitz Report", "https://www.newyorker.com/humor",
"Mueller Rents giant warehouse to store evidence against Trump", "Andy Borowitz")

popular_list = [p1, p2, p3]

@app.route("/article")
def article():
    return render_template("article.html", content = content_list, popular = popular_list)

if __name__ == "__main__":
    app.run(debug=True)