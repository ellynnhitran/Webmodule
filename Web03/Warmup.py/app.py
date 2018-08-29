from flask import Flask

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return "Hello " + name

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    total = a + b
    return str(total) #{0} + {1} = {2}.format(a, b, total)

if __name__ == "__main__":
    app.run(debug=True)