from app import db
from app.helpers import convert_to_slug
from app.models.Blog import Blog
from sqlalchemy import desc


class BlogController:
    def create_blog(self, form):
        """
        Fungsi untuk membuat Blog
        """
        title = form['title']
        content = form['content']
        tag = form['tag']

        blog = Blog(
            title=title,
            content=content,
            tag=tag,
            slug=convert_to_slug(title),
        )
        db.session.add(blog)
        db.session.commit()

    def edit_blog(self, blog, form):
        """
        Fungsi untuk meng-edit Blog
        """
        title = form['title']
        content = form['content']
        tag = form['tag']

        blog.title = title
        blog.content = content
        blog.tag = tag
        blog.slug = convert_to_slug(title)

        db.session.commit()

        return blog.slug

    def delete_blog(self, blog):
        """
        Fungsi untuk menghapus Blog
        """
        db.session.delete(blog)
        db.session.commit()
