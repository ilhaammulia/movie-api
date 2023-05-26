<<<<<<< HEAD
from flask import Blueprint, request, jsonify
from .. import db

from .. models.movies import *

from .. utils import errors
from uuid import uuid4

mod_movie = Blueprint('mod_movie', __name__, url_prefix='/api/movies')


# @mod_movie.route('/<:id>', methods=['GET'])
# def get_movie(id):
@mod_movie.route('/delete/<:id>', methods=['DELETE'])
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
=======
from flask import Blueprint, request

from .. import db 

from .. models.movies import Movie, Genre, Company

from .. utils import errors

from .. middlewares.authentications import login_required, admin_only

mod_movie = Blueprint('mod_movie', __name__, url_prefix='/api/movies')

@mod_movie.route('', methods=['GET'])
@login_required
def get_movies():
    movies = Movie.to_list()
    return {
        'error': None,
        'data': movies
    }

# @mod_movie.route('/<id>', methods=['GET'])
# @login_required
# def get_movie_byid(id):
#     movie = Movie.query.get(id)
#     if movie is None:
        
>>>>>>> 0b66847d3082dd8a3b1a2634c7ffb52fe201c269
