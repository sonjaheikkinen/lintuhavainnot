from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField

class SpeciesForm(FlaskForm):
    name = StringField("Lajinimi, kansakielinen (esim. talitiainen):")	
    species = StringField("Lajinimi, tieteellinen (esim. Parus major):")
    description = TextAreaField('Lajikuvaus:', render_kw={"rows": 10, "cols": 30})
 
    class Meta:
        csrf = False
