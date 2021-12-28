import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel # import the user model class helper

# This is a resource to add users
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        # Parse the arguments using the UserRegister, which expects a Username and password
        data = UserRegister.parser.parse_args()

        # Check if user name already exists
        if UserModel.find_by_username(data['username']):
            return {"message": "Username already exists"}, 404

        # user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()

        return {'Message': 'User successfully created.'}, 201
