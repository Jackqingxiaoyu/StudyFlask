from . import auth
from flask import request,sessions,make_response,render_template
from .forms import LoginForm
from app.models import User
from flask_login import login_user,logout_user,login_required
from flask import redirect,url_for
from flask_login import current_user
from .forms import RegiserForm
from app import db
from flask import flash
from app.email import send_mail
from flask import current_app

@auth.route("/confirm")
@login_required
def confirm():
    token = request.args.get("token")
    if current_user.check_token(token):
        return "激活成功"
    else:
        return "激活失败"

@auth.route("/register",methods=["GET","POST"])
def register():
    form = RegiserForm()
    if form.validate_on_submit():
        user = User()
        user.name = form.name.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash('恭喜《' + user.name + '》注册成功！' + '请登录！')
        # 发邮件
        temp = render_template('email/register_email.html', name=user.name, token=user.generate_token())
        send_mail('注册邮件', current_app.config['MAIL_USERNAME'], [user.email], None, temp)
        return redirect(url_for('.login'))
    return render_template('auth/register.html', form=form)

# http://127.0.0.1:5000/auth/confirm?id=sdfjkasfjfjsjfjfjfaj;afs

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))


# 127.0.0.1:5000/auth/login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # session['abc'] = '123456'
    # print(session)
    # print(request.cookies)
    # res = make_response('ok')
    # res.set_cookie('mycookie', '1', 60*60*24)
    # return res
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user, form.remember_me.data)
                return redirect(url_for('main.index'))
            else:
                form.password.errors.append('密码有误')
        else:
            form.email.errors.append('此用户不存在')

    return render_template('auth/login.html', form=form)

































