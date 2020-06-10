# flask
from flask import Flask
app = Flask(__name__)

# SQLAlchemy 
from flask_sqlalchemy import SQLAlchemy

# flask-bootsrap
from flask_bootstrap import Bootstrap
Bootstrap(app)

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///birds.db"    
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio
db = SQLAlchemy(app)

# Ladataan tietokantamallit
from application import models
from application.species import models
from application.auth import models 
from application.sightings import models 
from application.places import models

# Luodaan tietokantataulut
try: 
    db.create_all()
except:
    pass

# Lisataan tietokantaan testilintuja
from application import fillDatabase

# Kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message="Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Kayttajaroolit

from functools import wraps
def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", current_user.getRole()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

# Nakymat
from application import views
from application.species import views
from application.auth import views
from application.sightings import views
from application.places import views
