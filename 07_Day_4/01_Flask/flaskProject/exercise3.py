from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route('/')
def date():
    date_now = datetime.datetime.now().strftime('%A %B %d, %Y')
    return render_template("index3.html", date=date_now)

if __name__ == '__main__':
    app.run(debug=True)