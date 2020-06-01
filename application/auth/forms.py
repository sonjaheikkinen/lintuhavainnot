from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, validators
  
class Login(FlaskForm):
    username = StringField("Käyttäjätunnus:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    password = PasswordField("Salasana:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
  
    class Meta:
        csrf = False

class Registration(FlaskForm):
    name = StringField("Nimi:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    username = StringField("Käyttäjätunnus:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    password = PasswordField("Salasana:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    passwordConfirm = PasswordField("Kirjoita salasana uudestaan:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    info = TextAreaField("Lisätietoja:", render_kw={"rows": 10, "cols": 30})
  
    class Meta:
        csrf = False

class Edit(FlaskForm):
    name = StringField("Muuta nimeä:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    username = StringField("Vaihda käyttäjätunnus:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    info = TextAreaField("Muokkaa lisätietoja:", render_kw={"rows": 10, "cols": 30})
  
    class Meta:
        csrf = False

class Password(FlaskForm):
    password = PasswordField("Anna uusi salasana:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    passwordConfirm = PasswordField("Kirjoita salasana uudestaan:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    
    class Meta:
        csrf = False
