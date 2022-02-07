from datetime import datetime

from app import db
from flask_login import UserMixin
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import DateTime, Integer, String, Text


class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    avatar_url = Column(Text, nullable=True)
    name = Column(String(256), nullable=True)
    username = Column(String(256), nullable=False, unique=True)
    email = Column(String(256), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    role = relationship('Role')

    def get_created_at(self):
        return self.created_at.strftime("%B %d %Y")

    @staticmethod
    def get(username=None, email=None, id=None):
        '''
        Fungsi untuk mengambil data pengguna dari database
        '''
        if username:
            return User.query.filter_by(username=username).first()

        if email:
            return User.query.filter_by(email=email).first()

        if id:
            return User.query.filter_by(id=id).first()

        return None

    @staticmethod
    def count():
        return User.query.count()

    @staticmethod
    def get_all():
        return User.query.all()


class Role(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    @staticmethod
    def get(id=None, name=None):
        if id:
            return Role.query.filter_by(id=id).first()

        if name:
            return Role.query.filter_by(username=name).first()

        return None

    @staticmethod
    def get_default_role(id=2):
        return Role.query.filter_by(id=id).first()

    @staticmethod
    def get_all():
        return Role.query.all()
