from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.author import Authors, AuthorList
from resources.genre import Genre, GenreList

app = Flask(__name__)

app.config['SQLALCHEMY_DQTABASE_URI'] = "sqlit:///library.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'onii-chan yemete'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# @app.before_first_request
# def create_table(): db.create_all()

@app.before_first_request
def create_table():
    db.create_all()


api.add_resource(Genre, '/genre/<string:name>')
api.add_resource(GenreList, '/genre')
api.add_resource(Authors, '/author')
api.add_resource(AuthorList, '/authors/authorlist')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    #if config is None:
    #    app.config.from_object(config.BaseConfig)
    #else:
    #    app.config.from_object(config)
    app.run(port=5000, debug=True)