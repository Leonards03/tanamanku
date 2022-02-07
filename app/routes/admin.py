from app.controllers.AuthController import AuthController
from app.controllers.BlogController import BlogController
from app.controllers.PlantController import PlantController
from app.controllers.ProfileController import ProfileController
from app.forms import (BlogForm, ChangePasswordForm, EditProfileForm,
                       GenusForm, PlantForm, RegistrationForm, RoleForm,
                       UserProfileForm)
from app.middlewares.role_checker import check_permission
from app.models.Blog import Blog
from app.models.Plant import Genus, Plant
from app.models.User import Role, User
from flask import Blueprint, flash, request, url_for
from flask.helpers import make_response
from flask.templating import render_template
from flask_login import current_user, login_required
from werkzeug.utils import redirect

admin = Blueprint('admin', __name__)
blog_controller = BlogController()
plant_controller = PlantController()
auth_controller = AuthController()
profile_controller = ProfileController()

allowed_role = 'Admin'


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/')
def dashboard():
    view = render_template('pages/dashboard.html',
                           user_count=User.count(), plant_count=Plant.count(), blogs=Blog.get_all(), plants=Plant.get_all())
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/user')
def user_management():
    tab = request.args.get('tab') if request.args.get('tab') else 'user'

    users = User.query.all()
    roles = Role.query.all()
    view = render_template('pages/user-management.html',
                           users=users, roles=roles, tab=tab)
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/user/<int:id>')
def user_detail(id):
    view = render_template('pages/user-detail.html', user=User.get(id=id))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/user/create', methods=['GET', 'POST'])
def create_user():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            auth_controller.create_user(request.form)
            flash('Create user succesful', 'success')
            return redirect(url_for('admin.user_management'))
        except Exception as e:
            flash(f'{e}', 'danger')
        return redirect(request.referrer)

    view = render_template('pages/user-form.html', form=form,
                           operation='Create', action=url_for('admin.create_user'))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/user/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.get(id=id)
    if not user:
        flash('User not found', 'warning')
        return redirect(request.referrer)

    form = EditProfileForm(request.form, obj=user)
    form.role_id.choices = [(role.id, role.name) for role in Role.get_all()]

    if request.method == 'POST' and form.validate_on_submit():
        try:
            profile_controller.edit_profile(request.form, edited_user=user)
            flash('User information edited successfully!', 'success')
            return redirect(url_for('admin.user_management'))
        except Exception as e:
            flash(f'{e}', 'danger')
        return redirect(request.referrer)

    view = render_template('pages/user-form.html', form=form,
                           operation='Edit', action=url_for('admin.edit_user', id=id))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/user/delete/<int:id>', methods=['POST'])
def delete_user(id):
    try:
        user = User.get(id=id)
        if not user:
            flash('User not found', 'warning')
            return redirect(request.referrer)
        profile_controller.delete_account(user=user)
        flash('User deleted successfully', 'success')
    except Exception as e:
        flash(f'{e}', 'danger')

    return redirect(request.referrer)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/role/<int:id>')
def role_detail(id):
    view = render_template('pages/role-detail.html', role=Role.get(id))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/role/create', methods=['GET', 'POST'])
def create_role():
    form = RoleForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            profile_controller.create_role(request.form)
            flash('Role created succesfully', 'success')
            return redirect(url_for('admin.user_management', tab='role'))
        except Exception as e:
            flash(f'{e}', 'danger')
        return redirect(request.referrer)

    view = render_template('pages/role-form.html', form=form,
                           operation='Create', action=url_for('admin.create_role'))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/role/edit/<int:id>', methods=['GET', 'POST'])
def edit_role(id):
    role = Role.get(id=id)
    if not role:
        flash('Role not found', 'warning')
        return redirect(request.referrer)

    form = RoleForm(request.form, obj=role)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            profile_controller.edit_role(request.form)
            flash('Role information edited successfully!', 'success')
            return redirect(url_for('admin.user_management'))
        except Exception as e:
            flash(f'{e}', 'danger')
        return redirect(request.referrer)

    view = render_template('pages/user-form.html', form=form,
                           operation='Edit', action=url_for('admin.edit_user', id=id))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/role/delete/<int:id>', methods=['POST'])
def delete_role(id):
    try:
        role = Role.get(id=id)
        if not role:
            flash('Role not found', 'warning')
            return redirect(request.referrer)
        profile_controller.delete_role(role)
        flash('Role deleted successfully', 'success')
    except Exception as e:
        flash(f'{e}', 'danger')

    return redirect(request.referrer)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/plant')
def plant_management():
    tab = request.args.get('tab') if request.args.get('tab') else 'plant'

    plants = Plant.query.all()
    genuses = Genus.query.all()
    view = render_template('pages/plant-management.html',
                           plants=plants, genuses=genuses, tab=tab)
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/plant/<string:slug>')
def plant_detail(slug):
    view = render_template('pages/plant-detail.html', plant=Plant.get(slug))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/plant/create', methods=['GET', 'POST'])
def create_plant():
    form = PlantForm(request.form)
    form.genus_id.choices = [(genus.id, genus.name)
                             for genus in Genus.get_all()]
    if request.method == 'POST' and form.validate_on_submit():
        try:
            plant_controller.create_plant(request.form)
            flash('Plant information created successfully!', 'success')
            return redirect(url_for('admin.plant_management'))
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)
    view = render_template('pages/plant-form.html', form=form,
                           operation='Create', action=url_for('admin.create_plant'))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/plant/<string:slug>/edit', methods=['GET', 'POST'])
def edit_plant(slug):
    plant = Plant.get(slug)
    if not plant:
        flash('Plant not found', 'warning')
        return redirect(request.referrer)

    form = PlantForm(request.form, obj=plant)
    form.genus_id.choices = [(genus.id, genus.name)
                             for genus in Genus.get_all()]

    if request.method == 'POST' and form.validate_on_submit():
        try:
            plant_controller.edit_plant(plant, request.form)
            flash('Plant information edited successfully!', 'success')
            return redirect(url_for('admin.plant_management'))
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)
    view = render_template('pages/plant-form.html', form=form,
                           operation='Edit', action=url_for('admin.edit_plant', slug=plant.slug), image_url=plant.picture_url)
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/plant/<string:slug>/delete', methods=['POST'])
def delete_plant(slug):
    plant = Plant.get(slug)
    if not plant:
        flash('Plant not found', 'warning')
        return redirect(request.referrer)
    try:
        plant_controller.delete_plant(plant)
        flash('Plant information deleted successfully!', 'success')
    except Exception as e:
        flash(f'{e}', 'danger')
    return redirect(request.referrer)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/genus/<int:id>')
def genus_detail(id):
    view = render_template('pages/genus-detail.html', genus=Genus.get(id))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/genus/create', methods=['GET', 'POST'])
def create_genus():
    form = GenusForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            plant_controller.create_genus(request.form)
            flash('Genus created successfully!', 'success')
            return redirect(url_for('admin.plant_management', tab='genus'))
        except Exception as e:
            flash(f'{e}', 'danger')

        return redirect(request.referrer)

    view = render_template('pages/genus-form.html', form=form,
                           operation='Create', action=url_for('admin.create_genus'))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/genus/edit/<int:id>', methods=['GET', 'POST'])
def edit_genus(id):
    genus = Genus.get(id)
    if not genus:
        flash('Genus not found', 'warning')
        return redirect(request.referrer)

    form = GenusForm(request.form, obj=genus)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            plant_controller.edit_genus(genus, request.form)
            flash('Genus edited successfully!', 'success')
            return redirect(url_for('admin.plant_management', tab='genus'))
        except Exception as e:
            flash(f'{e}', 'danger')

        return redirect(request.referrer)

    view = render_template('pages/genus-form.html', form=form,
                           operation='Edit', action=url_for('admin.edit_genus', id=genus.id))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/genus/delete/<int:id>', methods=['POST'])
def delete_genus(id):
    genus = Genus.get(id)
    if not genus:
        flash('Genus not found', 'warning')
        return redirect(request.referrer)
    try:
        plant_controller.delete_genus(genus)
        flash('Genus deleted successfully', 'success')
    except Exception as e:
        flash(f'{e}', 'danger')

    return redirect(url_for('admin.plant_management', tab='genus'))


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/blog')
def blog_management():
    view = render_template('pages/blog-management.html', blogs=Blog.get_all())
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/blog/<string:slug>')
def blog_detail(slug):
    view = render_template('pages/blog-detail.html', blog=Blog.get(slug))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/blog/create', methods=['GET', 'POST'])
def create_blog():
    form = BlogForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            blog_controller.create_blog(request.form)
            flash('Blog created successfully!', 'success')
            return redirect(url_for('admin.blog_management'))
        except Exception as e:
            flash(f'{e}', 'danger')

        return redirect(request.referrer)

    view = render_template('pages/blog-form.html', form=form,
                           operation='Create', action=url_for('admin.create_blog'))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/blog/<string:slug>/edit', methods=['GET', 'POST'])
def edit_blog(slug):
    blog = Blog.get(slug=slug)
    if not blog:
        flash('Blog not found', 'warning')
        return redirect(request.referrer)

    form = BlogForm(request.form, obj=blog)

    if request.method == 'POST' and form.validate_on_submit():
        try:
            blog_controller.edit_blog(blog, request.form)
            flash('Blog edited successfully!', 'success')
            return redirect(url_for('admin.blog_management'))
        except Exception as e:
            flash(f'{e}', 'danger')

        return redirect(request.referrer)

    view = render_template('pages/blog-form.html', form=form,
                           operation='Edit', action=url_for('admin.edit_blog', slug=blog.slug))
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/blog/<string:slug>/delete', methods=['POST'])
def delete_blog(slug):
    blog = Blog.get(slug=slug)
    if not blog:
        flash('Blog not found', 'warning')
        return redirect(request.referrer)
    try:
        blog_controller.delete_blog(blog)
        flash('Blog deleted successfully', 'success')
    except Exception as e:
        flash(f'{e}', 'danger')

    return redirect(url_for('admin.blog_management'))


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/profile')
def profile():
    edit_profile_form = UserProfileForm(obj=current_user)
    change_password_form = ChangePasswordForm()
    view = render_template('pages/admin-profile.html',
                           edit_profile_form=edit_profile_form, change_password_form=change_password_form)
    return make_response(view)


@login_required
@check_permission(allowed_role=allowed_role)
@admin.route('/<string:username>/edit', methods=['GET', 'POST'])
def edit_profile(username):
    if current_user.username != username:
        flash('Unauthorized access!', 'warning')
        return redirect(request.referrer)

    form = EditProfileForm(request.form, obj=current_user)
    # Jika method POST dan form validasi saat submit
    if request.method == 'POST' and form.validate_on_submit():
        try:
            profile_controller.edit_profile(request.form)
            flash('Profile edited', 'success')
        except Exception as e:
            flash(f'{e}', 'danger')
        return redirect(request.referrer)
