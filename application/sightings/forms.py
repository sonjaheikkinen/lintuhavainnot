from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, validators

class AddSighting(FlaskForm):
    species = SelectField("Valitse havaittu laji:", choices=[(1, "sinitiainen")], coerce=int)
    info = TextAreaField("Lisätietoja havainnosta:", render_kw={"rows": 10, "cols": 30})

    class Meta:
        csrf = False


