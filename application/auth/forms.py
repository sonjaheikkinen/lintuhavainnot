from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus:")
    password = PasswordField("Salasana:")
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    name = StringField("Nimi:")
    username = StringField("Käyttäjätunnus:")
    password = PasswordField("Salasana:")
    info = TextAreaField("Lisätietoja:", render_kw={"rows": 10, "cols": 30})
  
    class Meta:
        csrf = False
