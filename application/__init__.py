# Tuodaan Flask
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy 
from flask_sqlalchemy import SQLAlchemy
# Kaytetaan birds.db-nimista SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, etta tiedosto sijaitsee taman sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///birds.db"
# Pyydetaan SQLAlchemya tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio
db = SQLAlchemy(app)

# Luetaan tiedostot

from application import views

from application.species import models
from application.species import views

# Luodaan tietokantataulu
db.create_all()
