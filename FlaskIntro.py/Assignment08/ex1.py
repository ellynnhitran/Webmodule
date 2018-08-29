from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello C4T4, this is homepage"
    
@app.route("/about-me")
def about_me():
    return '''
    1. Name: Tran Tue Nhi,
    2. Work: Student,
    3. School: Foreign Language Specialized School,
    4. Hobbies: Reading, traveling, writing, coding :)),
    5. Status: Single '''

@app.route("/school")
def school():
    return redirect("http://techkids.vn")

if __name__ == "__main__":
    app.run(debug=True)
