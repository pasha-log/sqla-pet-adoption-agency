from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension 
from flask_sqlalchemy import SQLAlchemy 
from models import db, connect_db, Adopt
from forms import AddPetForm, EditPetForm
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'bjsjsd945734')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all() 

@app.route('/')
def home_page(): 
    """Should list the pets"""
    pets = Adopt.query.all()
    return render_template("base.html", pets=pets) 

@app.route('/add', methods=["GET", "POST"])
def add_pet_form():
    """Create a form for adding pets. This should use Flask-WTF, and should have the following fields:
        Pet name
        Species
        Photo URL
        Age
        Notes 
    """
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data 
        notes = form.notes.data 
        available = form.available.data

        new_pet = Adopt(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(new_pet) 
        print(new_pet)
        db.session.commit()
        return redirect('/')
    else: 
        return render_template("add.html", form=form)

@app.route('/<int:id>', methods=["GET", "POST"])
def display_or_edit_pet(id):
    """Make a page that shows some information about the pet:

        Name
        Species
        Photo, if present
        Age, if present

        It should also show a form that allows us to edit this pet:

        Photo URL
        Notes
        Available

        This should be at the URL /[pet-id-number]. Make the homepage link to this.

    """
    pet = Adopt.query.get_or_404(id)
    form = EditPetForm()
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data 
        db.session.commit()
        return redirect('/')
    else:
        return render_template('detail-edit.html', form=form, pet=pet)

