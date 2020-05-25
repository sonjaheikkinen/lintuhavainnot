from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, validators
from application.species.models import Species

class AddSighting(FlaskForm):

    #species = Species.query.all()
    #choiceList = []
    #for species in species:
    #    choiceList.append((species.id, species.name))

    species = SelectField("Valitse havaittu laji:", coerce=int)
    info = TextAreaField("Lisätietoja havainnosta:", render_kw={"rows": 10, "cols": 30})

    class Meta:
        csrf = False


