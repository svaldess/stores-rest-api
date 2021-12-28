# import sqlite3
from db import db
# change class methods insert and update
# define by name is class method because returns an object of type ItemModel -> change methods in Resources/item.py
class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # back reference -> allows the store to see which items ara in items database
    items = db.relationship('ItemModel', lazy='dynamic') # this is a list of items -> many to one relationship
    # SQLAlchemy creates an object for each item. If we have many items, this could be expensive
    # use lazy='dynamic'

    def __init__(self, name):
        self.name = name

    # returns a JSON representation of the model
    def json(self):
        # return {'name': self.name, 'items': [item.json() for item in self.items]}
        # when using lazy='dynamic', self.items becomes a query builder
        # therefore, we need to add self.items.all()
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
