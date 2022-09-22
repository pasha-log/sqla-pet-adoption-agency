from flask_wtf import FlaskForm 
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
     
    name = StringField("name", validators=[InputRequired(message="Pet name required")]) 
    species = SelectField("species", choices=[("cat", "cat"), ("dog", "dog"), ("porcu", "porcupine")], validate_choice=False) 
    photo_url = StringField("photo_url", validators=[Optional(), URL(require_tld=True, message="Must be a url")]) 
    age = FloatField("age", validators=[Optional(), NumberRange(min=0, max=30, message="Must be between 0-30")]) 
    notes = StringField("notes", validators=[Optional()]) 
    available = BooleanField("This animal is available", default="checked")

class EditPetForm(FlaskForm): 

    photo_url = StringField("photo_url", validators=[Optional(), URL(require_tld=True, message="Must be a url")]) 
    notes = StringField("notes", validators=[Optional()]) 
    available = BooleanField("This animal is available", default="checked")
