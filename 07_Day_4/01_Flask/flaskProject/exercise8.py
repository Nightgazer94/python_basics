from flask import Flask, render_template_string, request, render_template

app = Flask(__name__)

numbers_request = """
    <!doctype html>
    <title>Calculator of Flask</title>
    <form method="post">
        Enter number: <input type="text" name="num1"><br>
        Enter number: <input type="text" name="num2"><br>
        Enter operator: <input type="text" name="operator"><br>
        <input type="submit" value="Calculate">
    </form>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operator = request.form['operator']

        if operator == '+':
            result = int(num1) + int(num2)
        elif operator == '-':
            result = int(num1) - int(num2)
        elif operator == '*':
            result = int(num1) * int(num2)
        elif operator == '/':
            result = int(num1) / int(num2)
        else:
            return "Invalid operator"
        return render_template("index8.html", result=f"{num1} {operator} {num2} = {result}")
    return render_template_string(numbers_request)

if __name__ == '__main__':
    app.run(debug=True)
