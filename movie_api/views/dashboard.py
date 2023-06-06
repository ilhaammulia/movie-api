from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import check_password_hash, generate_password_hash
from .. models.api_keys import APIKey
from .. models.users import User
from .. import db
import time


mod_dashboard = Blueprint('mod_dashboard', __name__, url_prefix='/')

@mod_dashboard.route('', methods=['GET'])
def dashboard():
    api_key = request.args.get('api_key')
    api_key = APIKey.query.filter_by(key=api_key).first()
    if not api_key:
        return redirect(url_for('mod_dashboard.login'))
    if api_key.user.username == 'admin':
        users = User.to_list()
        return render_template('admin.html', user=api_key.user, users=users)
    return render_template('index.html', user=api_key.user)

@mod_dashboard.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return redirect(url_for('mod_dashboard.login'))
        if not user.api_keys:
            new_api_key = APIKey(user_id=user.id, key=generate_password_hash(str(time.time()), method='sha256'))
            db.session.add(new_api_key)
            db.session.commit()
        return redirect(url_for('mod_dashboard.dashboard', api_key=user.api_key))
    return render_template('login.html')