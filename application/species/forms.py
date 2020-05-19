from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class SpeciesCreationForm(FlaskForm):
    name = StringField("Lajinimi, kansakielinen (esim. talitiainen):", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä."))])	
    species = StringField("Lajinimi, tieteellinen (esim. Parus major):", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    description = TextAreaField('Lajikuvaus:', render_kw={"rows": 10, "cols": 30})
 


    class Meta:
        csrf = False
