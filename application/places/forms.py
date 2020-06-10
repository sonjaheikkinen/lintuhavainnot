from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, validators

class Search(FlaskForm):

    name = StringField("Kirjoita hakusana:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])

    class Meta:
        csrf = False

class EditPlace(FlaskForm):

    name = StringField("Muuta nimeä:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    habitat = SelectMultipleField("Muuta paikkaan liitettyjä elinympäristöjä (pidä Ctrl-näppäin pohjassa tehdessäsi valintoja):", coerce=int)

    class Meta:
        csrf = False

class EditHabitat(FlaskForm):

    name = StringField("Muuta nimeä:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])

    class Meta:
        csrf = False

class AddHabitat(FlaskForm):

    name = StringField("Nimeä elinympäristö:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])

    class Meta:
        csrf = False