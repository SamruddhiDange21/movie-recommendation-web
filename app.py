from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("movies.csv")

@app.route("/", methods=["GET","POST"])
def home():

    movies = None
    message = ""

    if request.method == "POST":
        genre = request.form["genre"]

        movies = data[data["Genre"].str.lower() == genre.lower()]

        if movies.empty:
            message = "Sorry, we don't have movies for this genre."

    return render_template("index.html", movies=movies, message=message)

if __name__ == "__main__":
    app.run(debug=True)