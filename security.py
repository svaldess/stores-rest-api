# import lib to safe string compare (good for diff python versions)
from werkzeug.security import safe_str_cmp
# import User class
from models.user import UserModel

# function to autheticate user
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_userid(user_id)
