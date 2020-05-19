from flask_wtf import FlaskForm
from wtforms import StringField

class SpeciesForm(FlaskForm):
    name = StringField("Lajinimi, kansakielinen (esim. talitiainen)")
 
    class Meta:
        csrf = False
