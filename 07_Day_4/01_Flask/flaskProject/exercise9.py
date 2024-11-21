from flask import Flask, render_template_string,request
import random

app = Flask(__name__)

number_to_guess = random.randint(1,9)

number_request = """
    <!doctype html>
    <title>Guessing game</title>
    <form method="post">
        Enter number: <input type="text" name="user_num">
        <input type="submit" value="Send number">
    </form>
    <h3>{{ message }}<h3>
"""

@app.route('/',methods=['GET','POST'])
def game():
    message = ""
    global number_to_guess
    try:
        if request.method == "POST":
            user_num = int(request.form['user_num'])
            if number_to_guess < user_num:
                message = f"You must guess a number lower than {user_num}"
            elif number_to_guess > user_num:
                message = f"You must guess a number higher than {user_num}"
            else:
                message = "You guessed correctly! can you guess again"
                number_to_guess = random.randint(1,9)
        return render_template_string(number_request, message=message)
    except ValueError:
        return render_template_string(number_request, message="Invalid input")

if __name__ == '__main__':
    app.run(debug=True)



