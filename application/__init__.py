# flask
from flask import Flask
app = Flask(__name__)

# SQLAlchemy 
from flask_sqlalchemy import SQLAlchemy
# tietokanta
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///birds.db"
# tulostetaan SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio
db = SQLAlchemy(app)

#itse toteutetut toiminnallisuudet
from application import views

from application.species import models
from application.species import views

from application.auth import models 
from application.auth import views

#kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message="Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan tietokantataulut
db.create_all()
