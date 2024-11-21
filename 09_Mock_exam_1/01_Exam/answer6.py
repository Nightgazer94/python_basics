from flask import Flask, request
from exam import movies


app = Flask(__name__)

TEMP = """
    <!DOCTYPE html>
    <form method="POST">
        <h1>Insert title:</h1>
        <label for="movie"></label>
        <input type="text" id="movie" name="movie" placeholder="Insert your film here" />
        <input type="submit" value="Send to check">
    <form>
"""

@app.route("/movies/", methods=["POST", "GET"])
def movie_finder():
    if request.method == "GET":
        return TEMP
    else:
        movie = request.form["movie"]
        if movie in movies["favourite"]:
            return "Favourite"
        elif movie in movies["hated"]:
            return "Hated"
        else:
            return "Not in library"


if __name__ == "__main__":
    app.run(debug=True)