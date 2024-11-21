from flask import Flask,render_template
import random

app = Flask(__name__)

@app.route('/')
def lotto():
    numbers = [_ for _ in range(1, 50)]
    return render_template("index6.html", lotto=random.choices(numbers, k=6))

if __name__ == '__main__':
    app.run(debug=True)

