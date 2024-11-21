from flask import Flask,render_template_string,request

app = Flask(__name__)

request_name = """
    <!doctype html>
    <title>Greeting web</title>
    <form method="post">
        Enter your name: <input type="text" name="name">
        <input type="submit" value="Send name">
    </form>
"""

@app.route('/', methods=['GET', 'POST'])
def welcome_def():
    if request.method == 'POST':
        name = request.form['name']
        hello = f"Hello {name}"
        return render_template_string(hello)
    return render_template_string(request_name)

if __name__ == '__main__':
    app.run(debug=True)