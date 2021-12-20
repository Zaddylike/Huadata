from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:123@127.0.0.1:3306/mofangapp?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)

class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    username = db.Column(db.String(255), index=True, comment="用户名")
    password = db.Column(db.String(255), comment="登录密码")
    mobile = db.Column(db.String(15), index=True, comment="手机号码")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(255), index=True, comment="邮箱")
    created_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    updated_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.username)

# marshmallow转换数据格式主要通过架构转换类来完成．
# 在marshmallow使用过程中所有的架构转换类必须直接或间接继承于Schema基类
class UserSchema(ma.Schema):
    username = ma.String()
    mobile = ma.String()
    # sex = fields.Boolean()
    email = ma.Email()
    created_time = ma.DateTime()
    
@app.route("/")
def index():
    user = User(
        username="xiaoming",
        mobile="13312345677",
        sex=True,
        email="133123456@qq.com",
        created_time=datetime.now(),
        updated_time=datetime.now()
    )
    # 调用marsh把模型转换成python基本数据格式[字典/列表]
    us = UserSchema() # 序列化多个数据，可以使用many=True
    ret1 = us.dump(user)  # 格式化输出成字典
    ret2 = us.dumps(user)  # 格式化输出成json字符串
    print(">>>> us.dump(user)  --> 字典")
    print(ret1)
    print(">>>> us.dumps(user) --> json字符串")
    print(ret2)
    """运行结果：
    >>>> us.dump(user)  --> 字典
{'created_time': '2021-03-02T11:07:45.520209', 'updated_time': '2021-03-02T11:07:45.520221', 'username': 'xiaoming', 'email': '133123456@qq.com', 'sex': True, 'mobile': '13312345677'}

>>>> us.dumps(user) --> json字符串
{"created_time": "2021-03-02T11:07:45.520209", "updated_time": "2021-03-02T11:07:45.520221", "username": "xiaoming", "email": "133123456@qq.com", "sex": true, "mobile": "13312345677"}
    """
    print(type(ret1), type(ret2))

    user1 = User(
        username="xiaoming1号",
        mobile="13312345677",
        sex=True,
        email="133123456@qq.com",
        created_time=datetime.now(),
        updated_time=datetime.now()
    )

    user2 = User(
        username="xiaoming2号",
        mobile="13312345677",
        sex=True,
        email="133123456@qq.com",
        created_time=datetime.now(),
        updated_time=datetime.now()
    )

    user_list = [user,user1,user2]
    us = UserSchema()
    data_list = us.dump(user_list,many=True)
    print(data_list)
	"""
    运行结果：
	[{'mobile': '13312345677', 'created_time': '2021-03-02T11:12:50.128294', 'email': '133123456@qq.com', 'username': 'xiaoming'}, {'mobile': '13312345677', 'created_time': '2021-03-02T11:12:50.129576', 'email': '133123456@qq.com', 'username': 'xiaoming1号'}, {'mobile': '13312345677', 'created_time': '2021-03-02T11:12:50.129642', 'email': '133123456@qq.com', 'username': 'xiaoming2号'}]
	"""
    return "基本使用：模型序列化"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,host="0.0.0.0",port=5999)

