from db import db

class AuthorModel(db.Model):

    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String)

    def __init__(self, author):
        self.author = author

    def json(self):
        return {'author id' : self.id, 'name' : self.author}

    @classmethod
    def find_by_authorname(cls, name):
        return cls.query.filter_by(author=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()