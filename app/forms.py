from flask_wtf import FlaskForm
from wtforms import (BooleanField, EmailField, FileField, HiddenField,
                     PasswordField, SelectField, StringField, SubmitField,
                     TextAreaField)
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', id='username', validators=[
                           DataRequired()], render_kw={'placeholder': 'Username'})
    password = PasswordField('Password', id='password', validators=[
                             DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    name = StringField('Name', id='name', validators=[
                       DataRequired()], render_kw={'placeholder': 'John Doe'})
    username = StringField('Username', id='username',
                           validators=[DataRequired()], render_kw={'placeholder': 'JohnDoe68'})
    email = EmailField('Email', id='email', validators=[
                       DataRequired(), Email()], render_kw={'placeholder': 'johndoe@base.com'})
    password = PasswordField('Password', id='password',
                             validators=[DataRequired()], render_kw={'placeholder': 'Your password'})
    confirm_password = PasswordField('Confirm Password', id='confirm_password', validators=[
                                     DataRequired(), EqualTo('password', message='Confirmation password must match password')], render_kw={'placeholder': 'Must match password'})
    submit = SubmitField('Register')


class RoleForm(FlaskForm):
    id = HiddenField('Role', id='role-id')
    name = StringField('Role Name', id='role', validators=[DataRequired()])


class EditProfileForm(FlaskForm):
    name = StringField('Name', id='name')
    username = StringField('Username', id='username', validators=[
                           DataRequired()], render_kw={'placeholder': 'JohnDoe68'})
    email = EmailField('Email', id='email', validators=[
                       DataRequired(), Email()], render_kw={'placeholder': 'johndoe@base.com'})
    role_id = SelectField('Role', coerce=int)
    submit = SubmitField('Save Changes')


class UserProfileForm(FlaskForm):
    name = StringField('Name', id='name')
    username = StringField('Username', id='username', validators=[
                           DataRequired()], render_kw={'placeholder': 'JohnDoe68'})
    email = EmailField('Email', id='email', validators=[
                       DataRequired(), Email()], render_kw={'placeholder': 'johndoe@base.com'})
    submit = SubmitField('Save Changes')


class ChangePasswordForm(FlaskForm):
    password = PasswordField('Password', id='password',
                             validators=[DataRequired()], render_kw={'placeholder': 'Your secret password'})
    new_password = PasswordField('Password', id='new_password',
                                 validators=[DataRequired()], render_kw={'placeholder': 'Your secret password'})
    confirm_new_password = PasswordField('Confirm Password', id='confirm_new_password', validators=[
        DataRequired(), EqualTo('new_password', message='Confirmation password must match password')], render_kw={'placeholder': 'Must match password'})
    submit = SubmitField('Save Changes')


class PlantForm(FlaskForm):
    image = FileField('Plant Picture', id='plantImage',
                      render_kw={'accept': 'image/*'})
    name = StringField('Plant name', id='plant-name',
                       validators=[DataRequired()])
    description = TextAreaField(
        'Description', id='plant-description', validators=[DataRequired()], render_kw={'style': 'height:200px;'})
    species = StringField('Species', id='species', validators=[DataRequired()])
    genus_id = SelectField('Genus', coerce=int)


class GenusForm(FlaskForm):
    id = HiddenField('Genus id', id='genus-id')
    name = StringField('Genus Name', id='genus-name',
                       validators=[DataRequired()])
    description = TextAreaField(
        'Genus Description', id='genus-description', validators=[DataRequired()], render_kw={'style': 'height:200px;'})


class BlogForm(FlaskForm):
    id = HiddenField('Blog', id='blog-id')
    title = StringField('Title', id='blog-title', validators=[DataRequired()])
    content = TextAreaField('Content', id='content',
                            validators=[DataRequired()], render_kw={'style': 'height:200px;'})
    tag = StringField('Tag', id='tag')
