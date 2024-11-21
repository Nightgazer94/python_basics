from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello World!'

@app.route('/hello/<name>')
def say_hello(name):
    return render_template("index1.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)