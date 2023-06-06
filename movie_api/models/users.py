from .. import db
from . api_keys import APIKey

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))

    @property
    def api_keys(self):
        return [
            api.key for api in APIKey.query.filter_by(user_id=self.id).all()
        ]
    
    @property
    def api_key(self):
        return self.api_keys[0] if self.api_keys else ''
    
    @property
    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'api_key': self.api_keys
        }
    
    @classmethod
    def to_list(cls):
        users = cls.query.all()
        return [
            user.json for user in users
        ]