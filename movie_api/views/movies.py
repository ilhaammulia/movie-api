from datetime import datetime
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

    release_date_str = request.json.get('release_date')
    release_date = datetime.strptime(release_date_str, "%Y-%m-%d").date()

    language = request.json.get('language')
    popularity = request.json.get('popularity')
    synopsis = request.json.get('synopsis')    
    genres = request.json.get('genres', [])

    genre_objects = []

    for genre_name in genres:
        is_genres_exist = Genre.query.filter_by(name=genre_name).first()

        print(genre_name)
        if not is_genres_exist:
            genre = Genre(name=genre_name)
            db.session.add(genre)

            print('Berhasil menambah genre')
            
            db.session.commit()

            genre_objects.append(genre)
        else:
            genre_objects.append(is_genres_exist)

    if not all([id, title, release_date, language, popularity, synopsis, genres]):
        return errors.bad_request_form, 400
    
    is_movie_exist = Movie.query.filter_by(title=title).first()

    if is_movie_exist:
        return errors.movie_exists, 200    

    new_movie = Movie(id=id, title=title, release_date=release_date, language=language, popularity=popularity, synopsis=synopsis, genres=genre_objects)

    db.session.add(new_movie)
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
                "genres":genre_objects,
            }
        }, 201

@mod_movie.route('/<id>', methods=['PUT'])
@login_required
@admin_only
def update_movie(id):
    movie_id = Movie.query.get(id)
    title = request.json.get('title')
    release_date = request.json.get('release_date')
    language = request.json.get('language')
    popularity = request.json.get('popularity')
    synopsis = request.json.get('synopsis')
    genres = request.json.get('genres')

    if not movie_id:
        return errors.movie_not_found, 404
    if not all([movie_id, title, release_date, language, popularity, synopsis, genres]):
        return errors.bad_request_form, 400
    
    movie_id.title = title
    movie_id.release_date = release_date
    movie_id.language = language
    movie_id.popularity = popularity
    movie_id.synopsis = synopsis
    movie_id.genres.clear()
    for genre_name in genres:
        genre = Genre.query.filter_by(name=genre_name).first()
        if not genre:
            genre = Genre(name=genre_name)
        movie_id.genres.append(genre)
    db.session.commit()
    return {
        'error': None,
        'data': movie_id.json
    }, 200

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
