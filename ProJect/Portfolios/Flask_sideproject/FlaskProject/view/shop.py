from typing import NewType
from flask import (
    Flask,make_response,
    Blueprint,render_template,
    redirect,url_for,
    request,session
    )
from flask_restful import Api,Resource
# from flask_paginate import Pagination,get_page_parameter

from FlaskProject.model.user import User
from ..model.product import Product,ProductSchema
from ..model.db_shopcart import shopCart
from .. import db,call_back
import json
shop=Blueprint('shop',__name__)
api=Api(shop)


class Shop(Resource):
    def get(self):
        User.call_back()
        name=request.values.get('productName')
        startp=request.values.get('startp')
        endp=request.values.get('endp')
        sort=request.values.get('sort')

        productSchema= ProductSchema(many= True,only=['pid','name','price','url','photo_url']) #setting shcema define
        if sort=='up' or sort=='':
            method=Product.price.asc()
        else:
            method=Product.price.desc()

        if len(request.values)==0:
            productData=Product.query.order_by(method).all()
        elif name=="" and startp=="" and endp=="":
            productData=Product.query.order_by(method).all()
        elif len(name)==0 and len(startp)>0 and len(endp)>0:  
            productData=Product.query.filter((Product.price>=int(startp))&(Product.price<=int(endp))).order_by(method).all()
        elif len(name)>0 and len(startp)==0 and len(endp)==0:
            productData=Product.query.filter(Product.name.like(f'%{name}%')).order_by(method).all()
        else: #all of >0
            productData=Product.query.filter(Product.name.like(f'%{name}%')&(Product.price>=int(startp))&(Product.price<=int(endp))).order_by(method).all()
        outPut=productSchema.dump(productData) #serialzation

        total= len(Product.query.order_by(method).all())
        page = request.args.get('page', type=int, default=1)

        return make_response(render_template('shop.html',outPut=outPut,))

    def post(self):
        if call_back():
            try:
                checkItem=shopCart.query.filter((shopCart.productname==request.json.get("pn"))&(shopCart.uid==session.get('id'))).first()
                checkItem.productamount=int(checkItem.productamount)+int(request.json.get("num"))
                db.session.commit()
            except:
                request.json['uid']=session.get('id')
                newcarData=shopCart(request.json) #not necessary to deserialization
                db.session.add(newcarData)
                db.session.commit()
        else:
            return redirect(url_for('auth.loginPoint'))
        # return redirect(url_for('shopcart.shopcart11',cartoutPut=cartoutPut,))


api.add_resource(Shop,'/shop')

# has_next: 當前頁之後存在後續頁面時為真
# has_prev: 當前頁之前存在前置頁面時為真
# next_num: 下一頁的頁碼
# prev_num: 上一頁的頁碼



# {
#             "pn":request.json('pn'),
#             "pp":request.json('pp'),
#             "pid":request.json('pid'),
#             "num":request.json('num'),
#         }