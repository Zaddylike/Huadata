from flask import Flask,render_template,make_response,Blueprint,request,session,redirect,url_for
from flask_restful import Api,Resource

from ..model.user import User
from ..model.db_shopcart import shopCart
from .. import call_back,db


shopcart= Blueprint('shopcart',__name__)
api=Api(shopcart)

class Shopcart(Resource):
    def get(self):
        if call_back():
            print(User.get_user(session.get('user')))
            curUser=User.get_user(session.get('user'))
            curUsercar=shopCart.query.filter_by(uid=curUser.id).all()
            return make_response(render_template('shopcart.html',cartoutPut=curUsercar))
        else:
            return redirect(url_for('auth.loginPoint'))
    def post(self):
        curUser=User.get_user(session.get('user'))
        targetProduct=shopCart.query.filter((shopCart.uid==curUser.id)&(shopCart.productname==request.json.get('pn'))).first()
        if request.json.get("num")>targetProduct.productamount:
            return "NO"
        elif request.json.get("num")==targetProduct.productamount:
            db.session.delete(targetProduct)
            db.session.commit()
        else:
            targetProduct.productamount = int(targetProduct.productamount)-int(request.json.get("num"))
            db.session.commit()

api.add_resource(Shopcart,"/shopcart",endpoint='shopcart')