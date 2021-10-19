from flask import Flask
from imdb_api.apis import api

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run()