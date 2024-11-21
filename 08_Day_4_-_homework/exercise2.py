from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>ISBN Validator</title>
  </head>
  <body>
    <h1>Enter a 10-digit ISBN number:</h1>
    <form method="post" action="/">
      <input type="text" name="isbn" required>
      <button type="submit">Submit</button>
    </form>
    {% if result is not none %}
      <h2>{{ result }}</h2>
    {% endif %}
  </body>
</html>
'''


def is_valid_isbn(isbn):
    if len(isbn) != 10 or not isbn[:9].isdigit() or (isbn[-1] not in '0123456789X'):
        return False

    total = 0
    for i in range(9):
        total += (i + 1) * int(isbn[i])
    if isbn[-1] == 'X':
        total += 10 * 10
    else:
        total += 10 * int(isbn[-1])

    return total % 11 == 0


@app.route('/', methods=['GET', 'POST'])
def isbn_check():
    result = None
    if request.method == 'POST':
        isbn = request.form.get('isbn')
        if is_valid_isbn(isbn):
            result = 'Correct ISBN'
        else:
            result = 'Incorrect ISBN'
    return render_template_string(HTML_TEMPLATE, result=result)


if __name__ == '__main__':
    app.run(debug=True)
