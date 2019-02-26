from flask_wtf import FlaskForm
from wtforms.validators import Email,Length,DataRequired,Regexp,EqualTo
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from app.models import User
from wtforms.validators import ValidationError

class RegiserForm(FlaskForm):
    email = StringField(label="邮箱",validators=[
        DataRequired(message="必须填写邮箱"),
        Length(1,64,message="长度必须是1～64"),
        Email(message="必须为邮箱格式")
    ])
    name = StringField(label="昵称",validators=[
        DataRequired(message="必须填写昵称"),
        Length(1,64,message="长度必须是1～64"),
    ])
    password = PasswordField(label="设置密码",validators=[
        DataRequired(message='必须填写密码'),
        Length(6, 64, message='长须必须是6-64'),
        Regexp('^.*$', 0, message='密码必须包含xxx')
    ])
    password_again = PasswordField(label="确认密码",validators=[
        EqualTo("password",message="两次输入密码不一致")
    ])
    submit = SubmitField(label="注册")

    # 自定义校验方法
    def validate_email(self,field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            # 异常信息会被放到email的errors中
                raise ValidationError("此邮箱已经被注册")

    def validate_name(self,field):
        if field.data == "wangyuxin":
            # 异常信息会被放到name的errors中
                raise ValidationError("此名称为系统管理员，您无法使用！")


class LoginForm(FlaskForm):
    email = StringField(label="邮箱",validators=[
        DataRequired(message="必须填写邮箱"),
        Length(1,64,message="长度必须是1～64"),
        Email(message="必须是邮箱格式")
    ])

    password = PasswordField(label="密码",validators=[
        DataRequired(message="必须填写密码"),
        Length(6,64,message="长度必须是6～64"),
        # Regexp("^.*$",0,message="密码必须包含xxx")
    ])

    remember_me = BooleanField(label="记住密码",default=False)
    submit = SubmitField(label="登录")









































































