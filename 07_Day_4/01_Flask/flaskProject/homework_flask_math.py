from flask import Flask, request
import math

app = Flask(__name__)

template = '''
    <!doctype html>
    <title>Flask math</title>
    <h1>Flask math homework</h1>
    <form method = "post">
    Enter number: <input type="text" name="num">
    <input type="submit" value="Submit">
    </form> 
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        number = request.form.get('num')
        power_2 = int(number)**2
        power_n =int(number)**int(number)
        n_factorial = math.factorial(int(number))
        return (f"The {number} squared is {power_2}.<br>"
                f"The {number} raised to the power of {number} is {power_n}.<br>"
                f"The factorial of {number} is {n_factorial}.<br>")
    return template

if __name__ == '__main__':
    app.run(debug=True)

