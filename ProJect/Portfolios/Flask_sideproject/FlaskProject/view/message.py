from flask import Flask,Blueprint,make_response,render_template,request
from flask_restful import Api,Resource

from ..model.message import Message,MessageSchema
from .. import db,ValidationError

message =Blueprint('message',__name__)
api =Api(message)

Message_Schema=MessageSchema(many=False) #many=true

class MessageApi(Resource):
    def get(self):
        return make_response(render_template('message.html'))
    def post(self):
        try:
            print(request.form)
            messageData=Message_Schema.load(data=request.form,partial=True)
            print(messageData)
            print(type(messageData))
            newMessage=Message(messageData)
            db.session.add(newMessage)
            db.session.commit()    
            return make_response(render_template('message.html'))  
        except ValidationError as error:
            return make_response(f"ERROR:{error.messages}{error.valid_data}")
api.add_resource(MessageApi,'/write')