from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)


# user = User()
# user.password
# user.password = "123456"

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64))

    confimed = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.name + " " + str(self.id)

    @property
    def password(self):
        raise AttributeError("密码不可以读取")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create_super_user():
        user = User()
        user.email = '1205211194@qq.com'
        user.password = '123456'
        user.name = 'wangyuxinn'
        db.session.add(user)
        db.session.commit()

    # 生成token
    def generate_token(self):
        serializer = Serializer(current_app.config['SECRET_KEY'], 60 * 10)
        token = serializer.dumps({'user_id': self.id})
        return token

    # 解密token
    def check_token(self, token):
        serializer = Serializer(current_app.config['SECRET_KEY'], 60 * 10)
        try:
            data = serializer.loads(token)
        except:
            return False

        id = data.get('user_id')
        if id is None:
            return False
        if id != self.id:
            return False
        self.confimed = True
        db.session.add(self)
        db.session.commit()
        return True


from app import login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=int(id)).first()
