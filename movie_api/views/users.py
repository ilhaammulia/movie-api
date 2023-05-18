from flask import Blueprint, request
from werkzeug.security import check_password_hash

from .. models.users import User

from .. utils import errors

mod_auth = Blueprint('mod_auth', __name__, url_prefix='/api/users')

@mod_auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return errors.user_not_found
    return user.json

