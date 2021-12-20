from flask import session
from .. import db,ma

from marshmallow import validate #獨立import出來幫忙驗證 不然用flask_marshmallow來模具就好
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__='users'
    id= db.Column(db.Integer,primary_key= True)
    user= db.Column(db.String(30),unique= True,nullable= False,index= True)
    password_hash= db.Column(db.String(255),unique= False,nullable= False)
    insert_time= db.Column(db.DateTime,default= datetime.now)
    update_time= db.Column(db.DateTime,onupdate= datetime.now,default= datetime.now)

    #db.relationship
    userTocar= db.relationship("shopCart",backref= 'users')

    def __init__(self,User_DATA):
        self.user=User_DATA['user']
        self.password=User_DATA['password']

    @property
    def password(self):
        raise AttributeError('Password is not readabilty attribute')

    @password.setter
    def password(self,password):
        self.password_hash= generate_password_hash(password)

    @classmethod
    def get_user(cls,user):
        return cls.query.filter_by(user=user).first()

    @classmethod
    def call_back(cls):
        if session.get('user') and session.get('id'):
            print(session)
            return True
        else:
            session['user']=None
            session['id']=None
            session['authority']='visitor'
            print(session)
            return False

    def Check_Password(self,password):
        '''檢查密碼'''
        return check_password_hash(self.password_hash, password)

    def save_db(self):
        db.session.add(self)
        db.session.commit()

    def save_session(self):
        session['user'] = self.user
        session['Authority']= 'loginuser'
        session['id'] = self.id
        session.permanent= True

    @staticmethod
    def remove_session():
        session.pop('user',default= None)
        session.pop('id',default= None)
        session['Authority']= 'visitor'
        # session.clear()

    def __repr__(self) -> str:
        return super().__repr__()

class UserSchema(ma.Schema):
    user= ma.Str(required= True)
    # password= ma.Str(required= True,validate=[validate.Length(min=1,max=36)],)
    password= ma.Str(required= True)

'''
UserMixin幫我們記錄了四種用戶狀態：

is_authenticated
登入成功時return True(這時候才能過的了login_required)

is_active
帳號啟用並且登入成功的時候return True

is_anonymous
匿名用戶return True(登入用戶會return False)

get_id()
取得當前用戶id
'''