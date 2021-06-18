# main.py
from flask import Blueprint, redirect, url_for, request, flash, render_template
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from panel.model.UserModel import UserModel

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = UserModel.query.filter_by(email=email).first()
    print(user)
    if not user or not check_password_hash(user.password, password):
        flash('Sprawdz swoj login lub hasło i spróbuj ponownie')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('admin.index'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
