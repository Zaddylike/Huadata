import os
import datetime
from flask import Flask, request, session
import redis


class Config():
    #---session
    SECRET_KEY=os.urandom(24)
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=14)
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER= True
    # SESSION_PROTECTION= 'strong'
    SESSION_KEY_PREFIX = 'session:'
    SESSION_TYPE= 'redis'
    SESSION_REDIS= redis.Redis(host='127.0.0.1', port='6379', db=4)
    #---jwt
    # JWT_SECRET_KEY= 'this-is-any-key-you-setup'
    # JWT_ACCESS_TOKEN_EXPIRES= 3600 
    # JWT_COOKIE_CSRS_PROTECT= True
    # PROPAGATE_EXCEPTIONS = True

    #---sql
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI= "mysql+pymysql://root:efai2021@127.0.0.1:3306/flaskdb"
    
    #---other
    JSON_AS_ASCII= False
    UPLOSF_FOLDER=os.getcwd()
    
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    @staticmethod
    def transColor(c,text):
        if c=="ok":
            c=bcolors.OK
        elif c=="warning":
            c=bcolors.WARNING
        else:
            c=bcolors.FAIL
        return f"{c}{text}{bcolors.RESET}"