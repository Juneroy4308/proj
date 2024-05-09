from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    image_url = data[0]['url']
    return f'<img src="{image_url}" alt="cat">'

if __name__ == '__main__':
    app.run(debug=True)