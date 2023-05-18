from .. import db

class APIKey(db.Model):
    __tablename__ = 'api_keys'

    user_id = db.Column(db.String(255), db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    key = db.Column(db.String(255))
