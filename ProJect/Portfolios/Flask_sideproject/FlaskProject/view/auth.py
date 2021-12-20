from flask import (
    render_template, 
    request, 
    session, 
    Blueprint, 
    make_response,
    jsonify,
    )
from flask.helpers import url_for
from flask_restful import Api, Resource

from marshmallow import ValidationError
from werkzeug.utils import redirect
from ..model.user import User,UserSchema


auth= Blueprint('auth',__name__) #use with endpoint #blueprint import name
api= Api(auth)
User_SCHEMA=UserSchema() #many=True


class Signup(Resource):
    def get(self):
        return make_response(render_template('signup.html'))
    def post(self):
        User_DATA= User_SCHEMA.load(data=request.values, partial=True)
        try:
            User.get_user(User_DATA['user'])== None
        except:
            return "This account has been registered"
        try:
            New_USER= User(User_DATA)
            New_USER.save_db()
            New_USER.save_session()
            return jsonify({
                'code': 200,
                "message": "registration success,you must to login to get token",
                })
        except ValidationError as error:
            return jsonify({
                'errors': error.messages,
                "status code": 400
            })


class Login(Resource):
    def get(self):
        print(session)
        return make_response(render_template('login.html'))
    def post(self):
        try:
            User_DATA=User_SCHEMA.load(data=request.form, partial= True)
            user= User_DATA['user']
            password= User_DATA['password']
            print(user,password)
            curuser=User.get_user(user)
            if curuser.Check_Password(password) and curuser != None:
                curuser.save_session()
                print(jsonify({
                    'code': 200,
                    'message': 'Login success',
                    'user': curuser.user
                }))
                return redirect(url_for('index'))
            else:
                raise ValidationError("incorrect input")
        except ValidationError as error:
            return {
                'errors': repr(error)
            },400


class Logout(Resource):
    def get(self):
        User.remove_session()
        User.call_back()
        return jsonify({
            'msg': 'logout',
            'auth': session.get('Authority'),
            'status code': 200
        })


api.add_resource(Signup,'/signup')
api.add_resource(Login,'/login',endpoint='loginPoint')
api.add_resource(Logout,'/logout')