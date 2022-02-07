from app.controllers.AuthController import AuthController
from app.forms import EditProfileForm, LoginForm, RegistrationForm
from app.middlewares.auth_checker import check_if_authenticated
from flask import Blueprint, flash, make_response, redirect, request, url_for
from flask.helpers import make_response
from flask.templating import render_template
from flask_login import current_user, login_required, logout_user

auth = Blueprint('auth', __name__)
auth_controller = AuthController()


@auth.route('/login', methods=['GET', 'POST'])
@check_if_authenticated
def login():
    if current_user.is_authenticated:
        if current_user.role.name == 'Admin':
            return redirect(url_for('admin.dashboard'))
        return redirect(url_for('base.index'))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            auth_controller.authenticate(request.form)
            if current_user.role.name == 'Admin':
                return redirect(url_for('admin.dashboard'))
            else:
                return redirect(url_for('base.index'))

        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)

    view = render_template('pages/login.html', form=form)
    return make_response(view)


@auth.route('/register', methods=['GET', 'POST'])
@check_if_authenticated
def register():
    if current_user.is_authenticated:
        if current_user.role.name == 'Admin':
            return redirect(url_for('admin.dashboard'))
        return redirect(url_for('base.index'))
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            auth_controller.create_user(request.form)
            flash('Register successful, please login', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)

    if current_user.is_authenticated:
        return redirect(url_for('base.index'))

    view = render_template('pages/register.html', form=form)
    return make_response(view)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
