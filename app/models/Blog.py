from datetime import datetime

from app import db
from sqlalchemy import Column, desc
from sqlalchemy.types import DateTime, Integer, String, Text


class Blog(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    # merupakan campuran dari judul dan uuid sebagai alamat untuk
    # mengakses post, hal ini dilakukan untuk menghindari penggunaan id
    # yang mudah ditebak
    slug = Column(Text, nullable=False)
    tag = Column(String(64), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def get_created_at(self):
        import pytz  # $ pip install pytz
        # Untuk mengambil local timezone
        import tzlocal  # $ pip install tzlocal

        local_timezone = tzlocal.get_localzone()  # get pytz tzinfo
        local_time = self.created_at.replace(
            tzinfo=pytz.utc).astimezone(local_timezone)
        return local_time.strftime("%H:%M, %B %d %Y")

    @staticmethod
    def get(slug=None, id=id):
        if slug:
            return Blog.query.filter_by(slug=slug).first()
        if id:
            return Blog.query.filter_by(id=id).first()
        return None

    @staticmethod
    def get_all():
        return Blog.query.order_by(desc(Blog.created_at)).all()

    @staticmethod
    def get_paginated(page=1):
        return Blog.query.order_by(desc(Blog.created_at)).paginate(page, 5)
