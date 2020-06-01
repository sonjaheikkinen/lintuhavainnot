from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SelectMultipleField, TextAreaField, validators, widgets
from application.species.models import Species

class AddSighting(FlaskForm):

    species = SelectField("Valitse havaittu laji:", coerce=int)
    place = StringField("Havaintopaikka:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    habitats = SelectMultipleField("Valitse elinympäristöt (pidä Ctrl-näppäin pohjassa valitaksesi useampia vaihtoehtoja):", coerce=int)
    info = TextAreaField("Lisätietoja havainnosta:", render_kw={"rows": 10, "cols": 30})

    class Meta:
        csrf = False
    
    
    



