from datetime import datetime

from app import db
from app.models.User import Role, User
from flask import flash, session, url_for
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash, generate_password_hash


class ProfileController:
    """"Controller yang mengelola logika profil"""

    def edit_profile(self, form, edited_user=current_user):
        username = form.get('username', None)
        name = form.get('name', None)
        email = form.get('email', None)

        id = edited_user.id
        if edited_user.username != username:
            user = User.get(username=username)
            if user:  # check if username exists
                raise Exception('Username already used!')

        if edited_user.email != email:
            user = User.get(email=email)
            if user:  # check if email exists
                raise Exception('Email already used!')
        user = User.get(id=id)
        user.name = name
        user.username = username
        user.avatar_url = f'https://avatars.dicebear.com/api/initials/{user.username}.svg'
        user.email = email
        user.role_id = form.get('role_id', user.role_id)
        db.session.commit()

    def update_password(self, form):
        '''
        Fungsi untuk memperbaharui password
        '''
        user = User.get(current_user.username)
        password = form['password']
        new_password = form['new_password']
        confirm_new_password = form['confirm_new_password']

        # Mengecek apakah password sesuai
        if not check_password_hash(user.password, password):
            # Jika tidak maka beri alert password salah
            raise Exception('Wrong Password')

        if confirm_new_password != new_password:
            raise Exception(
                'Confirm password does not match with new password')

        user.password = generate_password_hash(new_password)
        db.session.commit()

    def delete_account(self, user=current_user):
        db.session.delete(user)
        db.session.commit()

    def create_role(self, form):
        name = form['name']

        role = Role()
        role.name = name

        db.session.add(role)
        db.session.commit()

    def edit_role(self, form):
        pass

    def delete_role(self, role):
        db.session.delete(role)
        db.session.commit()
