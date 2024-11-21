from flask import Flask, render_template, render_template_string

app = Flask(__name__)

@app.route('/')
def greeting():
    welcome = ("Welcome to the website for adding two numbers. "
                "To start, enter the URL (http://127.0.0.1:5000/count/number1/number2), "
                "replacing 'number1' and 'number2' with the numbers you want to add.")
    return render_template_string(welcome)

@app.route('/count/<int:number1>/<int:number2>')
def count(number1, number2):
    result = int(number1) + int(number2)
    return render_template("index4.html", sum=result)

if __name__ == '__main__':
    app.run(debug=True)