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