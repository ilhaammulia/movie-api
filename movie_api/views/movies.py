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
        
