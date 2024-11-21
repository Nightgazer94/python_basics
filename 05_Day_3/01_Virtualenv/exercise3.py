import requests

url = 'https://www.example.com'

response = requests.get(url)

if response.status_code == 200:

    html_code = response.text
    print(html_code)
else:
    print(f"Error: Unable to download the page. Status code: {response.status_code}")

