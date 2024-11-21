from flask import Flask, request, render_template_string
import math

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<html lang="en">
  <head>
    <title>Exercise 1</title>
  </head>
  <body>
    <h1>Enter a natural number</h1>
    <form method="POST" action="/">
      <input type="number" name="n" min="1" required>
      <input type="submit" value="Submit">
    </form>
    {% if results %}
    <h2>Results</h2>
    <table border="1">
      <tr><th>2^n</th><td>{{ results['2^n'] }}</td></tr>
      <tr><th>n^n</th><td>{{ results['n^n'] }}</td></tr>
      <tr><th>n!</th><td>{{ results['n!'] }}</td></tr>
    </table>
    {% endif %}
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        try:
            n = int(request.form['n'])
            results = {
                '2^n': 2 ** n,
                'n^n': n ** n,
                'n!': math.factorial(n)
            }
        except ValueError:
            results = None
    return render_template_string(HTML_FORM, results=results)

if __name__ == '__main__':
    app.run(debug=True)
