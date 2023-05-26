from functools import wraps
from .. models.api_keys import APIKey
from flask import request
from .. utils import errors

def login_required(func):
    @wraps(func)
    def check_api_key(*args, **kwargs):
        api_key = request.args.get('api_key')
        api_key = APIKey.query.filter_by(key=api_key).first()
        if not api_key:
            return errors.unauthorized, 401
        return func(*args, **kwargs)
    return check_api_key

def admin_only(func):
    @wraps(func)
    def is_admin(*args, **kwargs):
        api_key = request.args.get('api_key')
        api_key = APIKey.query.filter_by(key=api_key).first()
        if api_key.user.username != 'admin':
            return errors.forbidden, 200
        return func(*args, **kwargs)
    return is_admin