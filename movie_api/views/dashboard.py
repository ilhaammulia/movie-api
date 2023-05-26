from flask import Blueprint, render_template

mod_dashboard = Blueprint('mod_dashboard', __name__, url_prefix='')

@mod_dashboard.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('index.html')

@mod_dashboard.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')