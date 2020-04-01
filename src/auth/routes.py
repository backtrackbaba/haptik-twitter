from flask import redirect, url_for, flash, render_template, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from src import db
from src.auth import bp
from src.auth.forms import LoginForm
from src.auth.forms import SignUpForm
from src.models.user import User
from src.user.service import UserService


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('common.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user_service = UserService()
        user = user_service.get_user_from_username(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard.feed')
        return redirect(next_page)
    return render_template('pages/auth/login.html', form=form)


@bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, name=form.name.data)
        user.set_password(form.password.data)
        user.set_gravatar_url(form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('pages/auth/sign-up.html', title='Sign Up', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('common.home'))
