# -*- coding: utf-8 -*- 
from flask import Flask,session
from flask.helpers import make_response
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError,validate
from flask_session import Session
from flask_migrate import Migrate

from .config.config import Config,bcolors


db= SQLAlchemy()
ma= Marshmallow()
sion= Session()
mgt=Migrate()

def call_back():
    if session.get('user') and session.get('id'):
        print(session)
        return True
    else:
        session['user']=None
        session['id']=None
        session['authority']='visitor'
        print(session)
        return False

def create_app():
    #--define init
    app=Flask(__name__)
    try:
        app.config.from_object(Config)
        db.init_app(app) #Flask-SQLAlchemy must be initialized before Flask-Marshmallow.
        mgt.init_app(app,db)
        sion.init_app(app)
        ma.init_app(app)
        print(bcolors.transColor("ok","All Model initialization......Success"))
    except:
        print(bcolors.transColor("error","All Model initialization......Fail"))
    
    #--restfulapi
    from .view.auth import auth
    app.register_blueprint(auth, url_prefix= '/auth')

    from .view.ecPay import payment
    app.register_blueprint(payment,url_prefix= '/payment')

    from .view.shop import shop
    app.register_blueprint(shop,url_prefix= '/buysome')

    from .view.shopcart import shopcart
    app.register_blueprint(shopcart,url_prefix= '/buysome')

    from .view.message import message
    app.register_blueprint(message,url_prefix='/message')
    #pre-start
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if call_back():
            print(f"Hello {session['user'],session['id']}")
            return make_response(render_template('home.html'))
        try:
            db.create_all()
            print(bcolors.transColor("ok","All DataBase working......Success"))
        except:
            raise RuntimeError(bcolors.transColor("warning","DataBase not connect"))
        return make_response(render_template('home.html'))

    @app.route("/getSession",methods= ['GET'])
    def getSession():
        # print(session)
        # if session.get('user'):
        #     return make_response(session.get('Authority'))
        # return "OK"
        return make_response(render_template("test.html"))
    return app