from .. import db,ma,validate

class Message(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    username=db.Column(db.String(20))
    email=db.Column(db.String(200))
    contents=db.Column(db.String(200))
    def __init__(self,data):
        self.title=data['title']
        self.username=data['username']
        self.email=data['email']
        self.contents=data['contents']
        class Meta:
            __tablename__='message'
class MessageSchema(ma.Schema):
    title=ma.Str(required=True)
    username=ma.Str(required=True,validate=[validate.Length(min=1)])
    email=ma.Email(required=True)
    contents=ma.Str(required=True,validate=[validate.Length(min=10,max=199)])
    class Mata:
        orderd =True
