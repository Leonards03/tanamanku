from datetime import datetime

from app import db
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import desc
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import DateTime, Integer, String, Text


class Plant(db.Model):
    id = Column(Integer, primary_key=True)
    slug = Column(Text, nullable=False)
    picture_url = Column(Text, nullable=False)
    name = Column(String(256), nullable=False)
    description = Column(Text, nullable=False)
    species = Column(String(256), nullable=False)
    genus_id = Column(Integer, ForeignKey('genus.id'), nullable=False)
    genus = relationship('Genus')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    @staticmethod
    def get(slug=None, id=None):
        """
        Fungsi untuk mengambil informasi Plant
        """
        if slug:
            return Plant.query.filter_by(slug=slug).first()

        if id:
            return Plant.query.filter_by(id=id).first()

        return None

    @staticmethod
    def get_all():
        return Plant.query.all()

    @staticmethod
    def get_paginated(page=1):
        return Plant.query.paginate(page, 5)

    @staticmethod
    def count():
        return Plant.query.count()


class Genus(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    description = Column(Text, nullable=False)

    @ staticmethod
    def get(id=None):
        if id:
            return Genus.query.filter_by(id=id).first()
        return None

    @staticmethod
    def get_all():
        return Genus.query.all()

    @staticmethod
    def get_paginated(page=1):
        return Genus.query.paginate(page, 5)
