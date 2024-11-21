from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def numbers():
    nums = [random.randint(1, 100)for _ in range(3)]
    return render_template("index5.html", nums=nums)

if __name__ == '__main__':
    app.run(debug=True)

