from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class SpeciesCreationForm(FlaskForm):
    name = StringField("Lajinimi, kansakielinen (esim. talitiainen):", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])	
    species = StringField("Lajinimi, tieteellinen (esim. Parus major):", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    info = TextAreaField("Lajikuvaus:", render_kw={"rows": 10, "cols": 30})

    class Meta:
        csrf = False
 
class SpeciesEditForm(FlaskForm):
    name = StringField("Muokkaa nimeä:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")], default="test")	
    species = StringField("Muokkaa tieteellistä nimeä:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    info = TextAreaField("Muokkaa kuvausta:", render_kw={"rows": 10, "cols": 30})


    class Meta:
        csrf = False

