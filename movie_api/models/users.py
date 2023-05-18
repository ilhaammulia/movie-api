from .. import db
from . api_keys import APIKey

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))

    @property
    def api_key(self):
        return APIKey.query.filter_by(user_id=self.id).first()
    
    @property
    def json(self):
        return {
            'id': self.id,
            'api_key': self.api_key
        }