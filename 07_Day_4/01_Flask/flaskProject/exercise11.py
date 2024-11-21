from flask import Flask, render_template_string, request

app = Flask(__name__)

name_request = """
    <!doctype html>
    <title>Welcome user application</title>
    <form method="post">
        Enter your name: <input type="text" name="name"><br>
        Enter your surname: <input type="text" name="surname"><br>
        <input type="submit" value="Send name">
    </form>
"""

@app.route("/", methods=["GET", "POST"])
def greeting():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        welcome = f"Good morning {name} {surname}"
        return render_template_string(welcome)
    return render_template_string(name_request)

if __name__ == "__main__":
    app.run(debug=True)