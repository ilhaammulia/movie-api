from flask import Blueprint, request
from .. import db

from .. models.movies import *

from .. models.movies import Movie, Genre

from .. middlewares.authentications import login_required, admin_only

from .. utils import errors
from uuid import uuid4

mod_movie = Blueprint('mod_movie', __name__, url_prefix='/api/movies')

@mod_movie.route('', methods=['GET'])
@login_required
def get_movies():
    movies = Movie.to_list()
    return {
        'error': None,
        'data': movies
    }

@mod_movie.route('/<id>', methods=['GET'])
@login_required
def get_movie_byid(id):
    movie = Movie.query.get(id)
    if movie is None:
        return errors.movie_not_found, 404
    return movie.json, 200

@mod_movie.route('', methods=['POST'])
@login_required
def create_movie():
    id = str(uuid4())
    title = request.json.get('title')
    release_date = request.json.get('release_date')
    language = request.json.get('language')
    popularity = request.json.get('popularity')
    synopsis = request.json.get('synopsis')    
    genres = request.json.get('genres')

    is_genres_exist = Genre.query.filter_by(name=genres).first()

    if not is_genres_exist:
        genre = request.json.get('genres')
        genre = Genre(name=genre)
        db.session.add(genre)

        print('Berhasil menambah genre')
        
        db.session.commit()

    print(f'''
            id = {id} dengan type data {type(id)}     
            title = {title} dengan type data {type(title)}     
            release_date = {release_date} dengan type data {type(release_date)}     
            language = {language} dengan type data {type(language)}     
            popularity = {popularity} dengan type data {type(popularity)}     
            synopsis = {synopsis} dengan type data {type(synopsis)}     
            genres = {genres} dengan type data {type(genres)}     
    ''')

    if not all([id, title, release_date, language, popularity, synopsis, genres]):
        return errors.bad_request_form, 400
    
    is_movie_exist = Movie.query.filter_by(title=title).first()
    if is_movie_exist:
        return errors.movie_exists, 200    

    new_movie = Movie(id=id, title=title, release_date=release_date, language=language, popularity=popularity, synopsis=synopsis, genres=genres)

    print(new_movie.json)

    db.session.add(new_movie.json)
    db.session.commit()

    return {
        'error': None,
        'data': {
                "id":id,
                "title":title,
                "release_date":release_date,
                "language":language,
                "popularity":popularity,
                "synopsis":synopsis,
            }
        }, 201

@mod_movie.route('/<id>', methods=['DELETE'])
@login_required
@admin_only
def delete_movie(id):
    movie = Movie.query.get(id)
    if movie is None:
        return errors.movie_not_found, 404
    db.session.delete(movie)
    db.session.commit()

    return {
        'error': None,
        'data': {
            'id': id
        }
    }, 200
