import sqlite3
from db import db

# create a user object
# this is not a resource because API cannot receive/send data
# this is a helper that we use to store data about users
# this userModel is an API -> interface for another part of the program to interact with user

class UserModel(db.Model):
    # indicate SQLAlchemy what table and columns of the table with properties
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # autoincremental variable, it is automatically generated
    username = db.Column(db.String(80)) # 80 characters max
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_userid(cls, _id):
        return cls.query.filter_by(id=_id).first()
