from flask import Blueprint, request
from werkzeug.security import check_password_hash, generate_password_hash
from .. import db

from .. models.users import User
from .. models.api_keys import APIKey

from .. utils import errors
from uuid import uuid4
import time

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
    uid = str(uuid4())
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
    }, 201

@mod_auth.route('/<id>', methods=['PUT'])
@login_required
def update_user(id):
    user = User.query.get(id)
    username = request.json.get('username')
    password = request.json.get('password')
    if not user:
        return errors.user_not_found, 404
    if not all([username, password]):
        return errors.bad_request, 400
    is_exists = User.query.filter_by(username=username).first()
    if is_exists and user.id != is_exists.id:
        return errors.user_exists, 200
    user.username = username
    user.password = generate_password_hash(password)
    db.session.commit()
    return {
        'error': None,
        'data': {
            'id': user.id
        }
    }, 200

@mod_auth.route('/<id>', methods=['DELETE'])
@login_required
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return errors.user_not_found, 404
    db.session.delete(user)
    db.session.commit()
    return {
        'error': None,
        'data': {
            'id': user.id
        }
    }, 200

@mod_auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return errors.login_failed, 401
    if not user.api_keys:
        new_api_key = APIKey(user_id=user.id, key=generate_password_hash(str(time.time()), method='sha256'))
        db.session.add(new_api_key)
        db.session.commit()
    return user.json, 200
