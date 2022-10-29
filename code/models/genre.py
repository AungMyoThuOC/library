from db import db

class GenreModel(db.Model):

    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key = True)
    genre = db.Column(db.String)

    def __init__(self, genre):
        self.genre = genre

    def json(self):
        return {'Genre id' : self.id, 'Genre' : self.genre}

    @classmethod
    def find_genre_by_name(cls, genre):
        return cls.query.filter_by(genre=genre).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()