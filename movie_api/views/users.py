from flask import Blueprint, request
from werkzeug.security import check_password_hash, generate_password_hash
from .. import db

from .. models.users import User

from .. utils import errors
from uuid import uuid4

from .. middlewares.authentications import login_required, admin_only

mod_auth = Blueprint('mod_auth', __name__, url_prefix='/api/users')

@mod_auth.route('', methods=['GET'])
@login_required
@admin_only
def get_users():
    users = User.to_list()
    return {
        'error': None,
        'data': users
    }, 200

@mod_auth.route('', methods=['POST'])
def create_user():
    uid = uuid4()
    username = request.json.get('username')
    password = request.json.get('password')
    if not all([username, password]):
        return errors.bad_request, 400
    is_exists = User.query.filter_by(username=username).first()
    if is_exists:
        return errors.user_exists, 200
    new_user = User(id=uid, username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return {
        'error': None,
        'data': {
            'id': new_user.id
        }
    }

@mod_auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return errors.user_not_found, 404
    return user.json, 200
