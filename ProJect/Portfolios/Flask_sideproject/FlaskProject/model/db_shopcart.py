from .. import db,ma

class shopCart(db.Model):
    __tablename__='shopcart'
    cid=db.Column(db.Integer,primary_key=True)
    productname=db.Column(db.String(100))
    productprice=db.Column(db.Integer)
    productamount=db.Column(db.String(99))
    
    #db.foreignkey
    uid= db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    pid= db.Column(db.Integer, db.ForeignKey('product.pid'),nullable=False)

    class Meta:
        __tablename__='shopcart'

    def __init__(self, data):
        self.productname=data['pn']
        self.productprice=data['pp']
        self.productamount=data['num']
        self.uid=data['uid']
        self.pid=data['pid']