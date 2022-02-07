from app.models.Blog import Blog
from app.models.Plant import Plant
from flask import Blueprint
from flask.helpers import make_response
from flask.templating import render_template
from flask_login import current_user

base = Blueprint('base', __name__)


@base.route('/')
def index():
    view = render_template('pages/home.html')
    return make_response(view)


@base.route('/blog')
def blogs():
    view = render_template('pages/blogs.html', blogs=Blog.get_all())
    return make_response(view)


@base.route('/blog/<string:slug>')
def blog(slug):
    view = render_template('pages/blog.html', blog=Blog.get(slug=slug))
    return make_response(view)


@base.route('/plant')
def plants():
    view = render_template('pages/plants.html', plants=Plant.get_all())
    return make_response(view)


@base.route('/plant/<string:slug>')
def plant(slug):
    view = render_template('pages/plant.html', plant=Plant.get(slug=slug))
    return make_response(view)
