# cd Documents/Trainings/Rest_APIs/5
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# Flask will be the app
app = Flask(__name__)
# tell SQLAlchemy that data.db lives at the route folder of the project
# can be MyOrale, SQL, etc. instead of sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# turn off tracking of modifications from flask. Does not tyurn off the SQLAlchemy tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# add secret key for authentication
app.secret_key = "svs"
# add resources from flask to Api
api = Api(app)

# use a Flask decorator to create table before the first Request
# Use this to substitute create_tables.py
@app.before_first_request
def create_tables():
    db.create_all()

# call jwt for authentication
jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# when importing app.py in another file, we use the following line to
# prevent running the app. Only importing the lines above.
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    # use debug= True to get more information in case we gat an error
    app.run(port=5000, debug=True)
