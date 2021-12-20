from .. import db,ma

from datetime import datetime


class Product(db.Model):
    __tablename__='product'
    # __table_args__ = {'extend_existing': True} 
    pid= db.Column(db.Integer,primary_key= True)
    name= db.Column(db.String(30))
    price= db.Column(db.Integer)
    url= db.Column(db.String(250))
    photo_url= db.Column(db.String(250))

    #db.relationship
    productTocar=db.relationship("shopCart",backref='product')

class ProductSchema(ma.Schema):
    pid= ma.Str(required=False)
    name= ma.Str(required=False)
    price= ma.Integer(required= False)
    url= ma.Str(required= False)
    photo_url= ma.Str(required= False)
