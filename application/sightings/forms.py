from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class AddSighting(FlaskForm):
    info = TextAreaField("Lisätietoja havainnosta:", render_kw={"rows": 10, "cols": 30})

    class Meta:
        csrf = False


