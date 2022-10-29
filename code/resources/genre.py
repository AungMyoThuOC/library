from flask_restful import Resource, reqparse
# from flask_jwt import jwt_required
from flask import request
from models.genre import GenreModel

class Genre(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "genre",
        type = str,
        required = True,
        help = "This field can't be blank!"
    )

    def get(self):
        data = request.get_json()

        genre = GenreModel.find_genre_by_name(data['name'])

        if genre:
            return genre.json()

        return {"message" : "Genre not exist"}, 401

    def post(self, name):
        genre = GenreModel.find_genre_by_name(name)

        if genre:
            return {"message" : "Genre with this name {} already exist!".format(name)}, 400
        
        data = Genre.parser.parse_args()
        genre = GenreModel(name, data['name'])

        try:
            genre.save_to_db()
        except:
            return {"message" : "An error occured while insertiong data!"}, 500

        return genre.json(), 201

    def delete(self, name):
        gener = GenreModel.find_genre_by_name(name)

        if gener:
            GenreModel.delete_from_db()

        return {"message" : "Genre delete successfully!"}, 201

    def put(self, name):
        date = Genre.parser.parse_args()

        genre = GenreModel.find_genre_by_name(name)

        if genre is None:
            genre = GenreModel(name, date['name'])
        
        genre.save_to_db()

        return genre.json()

class GenreList(Resource):
    def get(self):
        genres = GenreModel.quary.all()
        return {"Genre" : [genre.json() for genre in genres]}