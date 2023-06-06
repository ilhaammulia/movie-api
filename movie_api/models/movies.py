from uuid import uuid4

from .. import db 
from . api_keys import APIKey
    
movie_genre = db.Table('movie_genre',
                       db.Column('movie_id', db.String(255), db.ForeignKey('movies.id')),
                       db.Column('genre_id', db.String(255), db.ForeignKey('genres.id')),
                       )

class Genre(db.Model):
    __tablename__ = 'genres' 

    id = db.Column(db.String, primary_key=True, default=str(uuid4()))
    name = db.Column(db.String)

    @property
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.Date)
    language = db.Column(db.String)
    popularity = db.Column(db.Float)
    synopsis = db.Column(db.Text)

    # relations
    genres = db.relationship('Genre', secondary=movie_genre, backref='movie', lazy=True)

    @property
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'language': self.language,
            'genres': [genre.name for genre in self.genres],
            'popularity': self.popularity,
            'synopsis': self.synopsis,
        }
    
    @classmethod
    def to_list(cls):
        movies = cls.query.all()
        return [
            movie.json() for movie in movies
        ]
