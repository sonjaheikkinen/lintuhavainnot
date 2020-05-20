from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    password = PasswordField("Salasana:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    name = StringField("Nimi:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    username = StringField("Käyttäjätunnus:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    password = PasswordField("Salasana:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    info = TextAreaField("Lisätietoja:", render_kw={"rows": 10, "cols": 30})
  
    class Meta:
        csrf = False
