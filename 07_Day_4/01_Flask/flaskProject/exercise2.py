from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route('/')
def time():
    time_now = datetime.datetime.now().strftime("%I:%M %p")
    return render_template("index2.html", time = time_now)

if __name__ == '__main__':
    app.run(debug=True)