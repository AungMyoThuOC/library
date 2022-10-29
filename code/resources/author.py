from models.author import AuthorModel
from flask_restful import Resource, reqparse
from flask import jsonify, request

class Authors(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'authorname',
        type = str,
        required = True,
        help = "This field can't be blank!"
    )

    def get(self):
        authors = AuthorModel.quary.all()
        return {"Author" : [author.json() for author in authors]}

    def post(self):
        data = Authors.parser.parse_args()
        author = AuthorModel.find_by_authorname(data['name'])

        if author:
            return{"message" : "{} already exists.".format(data['name'])}, 400

        author = AuthorModel(data["name"])
        try:
            author.save_to_db()
        except:
            {"message" : "Error occours."}, 400

        return author.json(), 201

    def put(self):
        data = Authors.parser.parse_args()
        author = AuthorModel.find_by_authorname(data['name'])

        if author is None:
            author = AuthorModel(data["name"])
        author.save_to_db()

        return{"message" : "update successfully"}

    def delete(self):
        data = request.get_json()
        author = AuthorModel.find_by_authorname(data['name'])
        if author:
            author.delete_from_db()
        return {"message" : "Author name delete successfully."}

class AuthorList(Resource):
    def get(self):
        authors = AuthorModel.quary.all()
        return {"authors" : [author.json() for author in authors]}