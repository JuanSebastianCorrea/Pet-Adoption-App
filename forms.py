"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form to register/post animal for adoption."""

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('dog', 'Dog'), ('fish', 'Fish'), ('bird', 'Bird'), ('cat', 'Cat')])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = FloatField("Age (years)", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")
    
    

    
