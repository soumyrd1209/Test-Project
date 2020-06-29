import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='username cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='password cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"Error Message": "User with name {} already exists".format(data["username"])}, 400
        user = UserModel(None,**data)
        try:
            user.save_to_db()
        except:
            return {"Error Message": "Failed to create user"}, 500
        return {"Message": "User Created Successfully"}, 201
