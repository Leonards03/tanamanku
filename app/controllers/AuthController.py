from datetime import timedelta

from app import db, mail
from app.config import Config
from app.models.User import Role, User
from flask import flash, session
from flask_login import current_user, login_user
from flask_mail import Message
from werkzeug.security import check_password_hash, generate_password_hash


class AuthController:
    """  
    Controller yang mengelola otentikasi 

    """

    @staticmethod
    def check_username_and_email(username, email):
        """
        Fungsi untuk mengecek apakah username atau email sudah digunakan
        """
        user = User.get(username)
        if user:  # check if username exists
            raise Exception('Username already used!')

        user = User.get(email=email)
        if user:  # check if email exists
            raise Exception('Email already used!')

    def create_user(self, form):
        """
        Fungsi untuk membuat user/akun baru
        """
        email = form['email']
        name = form.get('name', None)
        username = form['username']
        password = form['password']
        confirm_password = form['confirm_password']

        if password != confirm_password:  # Assert if both contains the same password
            raise Exception('Confirmation Password does not match Password')

        AuthController.check_username_and_email(username, email)

        default_role = Role.get_default_role()

        user = User()
        user.username = username
        user.email = email
        user.name = name
        user.avatar_url = f'https://avatars.dicebear.com/api/initials/{username}.svg'
        user.password = generate_password_hash(form['password'])
        user.role_id = default_role.id
        db.session.add(user)
        db.session.commit()

        mail_message = Message(subject='Welcome to TanamanKu Community!',
                               sender='tanamanku.community@gmail.com', recipients=[email])
        mail_message.body = """
        Explore your favorite plant here.
        """.strip()

        try:
            mail.connect()
            mail.send(mail_message)
        except Exception as e:
            flash(f'{e}', 'danger')

    def authenticate(self, form):
        """
        Fungsi untuk otentikasi/login
        """
        username = form['username']
        password = form['password']

        user = User.get(username)
        if not user:
            raise Exception('Username or Password is invalid!')

        if not check_password_hash(user.password, password):
            raise Exception('Username or Password is invalid!')

        logged_in = login_user(user, duration=timedelta(days=3))

        if logged_in:
            flash(f'Welcome {user.username}!', 'success')
            session['username'] = user.username
            session['name'] = user.name
            session['role'] = user.role.name
            session['logged_in'] = True
            session.permanent = False
