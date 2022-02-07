import os

from app import db
from app.config import Config
from app.helpers import allowed_file, convert_to_slug
from app.models.Plant import Genus, Plant
from flask import flash, redirect, request, url_for
from werkzeug.utils import secure_filename


class PlantController:
    def create_plant(self, form):
        name = form['name']
        description = form['description']
        species = form['species']
        genus_id = form['genus_id']

        plant = Plant()
        plant.slug = convert_to_slug(name)
        plant.picture_url = ''
        file = request.files['image']
        try:
            if file:
                flash('File exist', 'success')
                if file.filename == '':
                    flash('File not chosen!', 'warning')

                filename = secure_filename(file.filename)
                ext = filename.rsplit('.', 1)[1].lower()
                save_filename = f'{plant.slug}.{ext}'
                UPLOAD_FOLDER = os.path.realpath(
                    '.') + '\\app\\public\\uploads'
                file.save(os.path.join(UPLOAD_FOLDER, save_filename))
                plant.picture_url = save_filename
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)
        plant.name = name
        plant.description = description
        plant.species = species
        plant.genus_id = genus_id

        db.session.add(plant)
        db.session.commit()

        return plant.slug

    def edit_plant(self, plant, form):
        name = form['name']
        description = form['description']
        species = form['species']
        genus_id = form['genus_id']

        plant.slug = convert_to_slug(name)
        plant.picture_url = ''
        file = request.files['image']
        try:
            if file:
                if file.filename == '':
                    flash('File not chosen!', 'warning')

                filename = secure_filename(file.filename)
                ext = filename.rsplit('.', 1)[1].lower()
                save_filename = f'{plant.slug}.{ext}'
                UPLOAD_FOLDER = os.path.realpath(
                    '.') + '\\app\\public\\uploads'
                file.save(os.path.join(UPLOAD_FOLDER, save_filename))
                plant.picture_url = save_filename
        except Exception as e:
            flash(f'{e}', 'danger')
            return redirect(request.referrer)
        plant.name = name
        plant.description = description
        plant.species = species
        plant.genus_id = genus_id

        db.session.commit()

        return plant.slug

    def delete_plant(self, plant):
        db.session.delete(plant)
        db.session.commit()

    def create_genus(self, form):
        name = form['name']
        description = form['description']

        genus = Genus()
        genus.name = name
        genus.description = description

        db.session.add(genus)
        db.session.commit()

    def edit_genus(self, genus, form):
        genus.name = form['name']
        genus.description = form['description']
        db.session.commit()

    def delete_genus(self, genus):
        db.session.delete(genus)
        db.session.commit()
