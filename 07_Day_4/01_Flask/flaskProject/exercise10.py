from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "You use GET method"
    elif request.method == 'POST':
        return "You use POST method"

if __name__ == '__main__':
    app.run(debug=True)