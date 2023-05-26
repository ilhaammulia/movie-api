from .. import db 
from . api_keys import APIKey

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.Date)
    language = db.Column(db.String)
    vote_averages = db.Column(db.Float)
    vote_count = db.Column(db.Integer)
    popularity = db.Column(db.Float)
    synopsis = db.Column(db.Text)
    budget = db.Column(db.Integer)
    revenue = db.Column(db.Integer)
    runtime = db.Column(db.Integer)
    tagline = db.Column(db.Text)

    # relations
    genres = db.relationship('Genre', backref='movie', lazy=True)
    companies = db.relationship('Company', backref='movie', lazy=True)

    @property
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'language': self.language,
            'genres': [genre.json for genre in self.genres],
            'vote_averages': self.vote_averages,
            'vote_count': self.vote_count,
            'popularity': self.popularity,
            'synopsis': self.synopsis,
            'budget': self.budget,
            'revenue': self.revenue,
            'runtime': self.runtime,
            'tagline': self.tagline,
            'companies': [companie.json for companie in self.companies],
        }

class Genre(db.Model):
    __tablename__ = 'genres' 

    id = db.Column(db.String(primarykey=True))
    name = db.Column(db.String)

    @property
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.String(primary_key=True))
    name = db.Column(db.String)

    @property
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

