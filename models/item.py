# import sqlite3
from db import db
# change class methods insert and update
# define by name is class method because returns an object of type ItemModel -> change methods in Resources/item.py
class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    # add new column for stores
    # store id should match store id in database
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel') # find a store in database that matches the store id

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    # returns a JSON representation of the model
    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # SQLAlchemy query -> SELECT * FROM itmes WHERE name = name LIMIT 1
        # returns an ItemModel object
        # return ItemModel.query.filter_by(name=name).first()
        return cls.query.filter_by(name=name).first()

    # this method is useful for both insert and update
    def save_to_db(self):
        # a session is a collection of objects in a database
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
