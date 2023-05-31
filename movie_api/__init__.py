from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
db = SQLAlchemy()


def create_app():
  global app

  app = Flask(__name__)

  app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')

  db.init_app(app)

  from . views.users import mod_auth
  from . views.movies import mod_movie

  from . views.dashboard import mod_dashboard

  app.register_blueprint(mod_auth)
  app.register_blueprint(mod_movie)
  app.register_blueprint(mod_dashboard)


  with app.app_context():
      db.create_all()
  
  return app


