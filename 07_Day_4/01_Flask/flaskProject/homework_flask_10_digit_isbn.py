from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!doctype html>
<html>
<head><title>ISBN Checker</title></head>
<body>
  <h1>ISBN Validator</h1>
  <form method="post">
    <label for="isbn">Enter ISBN:</label>
    <input type="text" name="isbn" id="isbn" maxlength="10" required>
    <button type="submit">Check ISBN</button>
  </form>
  {% if result is not none %}
    <h2>{{ result }}</h2>
  {% endif %}
</body>
</html>
"""

def is_valid_isbn(isbn):
    if len(isbn) != 10 or not isbn[:-1].isdigit() or (isbn[-1] not in '0123456789X'):
        return False

    total = 0
    for i in range(9):
        total += (i + 1) * int(isbn[i])

    if isbn[9] == 'X':
        total += 10 * 10
    else:
        total += 10 * int(isbn[9])

    return total % 11 == 0

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        isbn = request.form.get("isbn")
        if is_valid_isbn(isbn):
            result = "Correct ISBN"
        else:
            result = "Incorrect ISBN"
    return render_template_string(html_template, result=result)

if __name__ == "__main__":
    app.run(debug=True)
