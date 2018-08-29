from flask import Flask, render_template

app = Flask(__name__)

class Book:
    def __init__(self, t, a,tu, c, r):
        self.title = t
        self.author = a
        self.thumbnail_url = tu
        self.content = c
        self.rating = r

@app.route("/")
def index():
    return render_template("index.html", name="Nhi", 
    image_url="https://i.pinimg.com/564x/d1/54/cc/d154cca7aeb121d0b9bb07306af4d9f8.jpg")

b1 = Book("Angels and Demons",
"Dan Brown",
"https://images-na.ssl-images-amazon.com/images/I/81adkKbGZgL.jpg",
"Angels & Demons shares many stylistic literary elements with its sequels, such as conspiracies of secret societies, a single-day time frame, and the Catholic Church. Ancient history, architecture, and symbology are also heavily referenced throughout the book. A film adaptation was released on May 15, 2009.",
"3.87/5 (Goodreads)")

b2 = Book("Da Vinci Code",
"Dan Brown",
"https://images-eu.ssl-images-amazon.com/images/I/5171w-4D2FL.jpg",
"The title of the novel refers to the finding of the first murder victim in the Grand Gallery of the Louvre, naked and posed similar to Leonardo da Vinci's famous drawing, the Vitruvian Man, with mathematic message written beside his body and a pentagram drawn on his chest in his own blood.",
"3.81/4 (Goodreads)")

b3 = Book("Origin",
'Dan Brown',
"https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Origin_%28Dan_Brown_novel_cover%29.jpg/220px-Origin_%28Dan_Brown_novel_cover%29.jpg",
"Edmon Kirsch informs them that he has made a revolutionary discovery that he plans to release to the public in a month. He is advising them out of supposed respect, despite his well known hatred of organized religion which he blames for his mother's death. Horrified, the three learn that he is presenting it in three days' time, prompting Valdespino to send him a voice mail demanding that he stop or risk being discredited.",
"3.84/4 (Goodreads)")

book_list = [b1, b2, b3]

@app.route("/book")
def book():
    return render_template("book.html", books = book_list)

if __name__ == "__main__":
    app.run(debug=True)