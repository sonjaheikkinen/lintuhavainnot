# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
# Käytetään birds.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, että tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///birds.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio
db = SQLAlchemy(app)

# Luetaan tiedostot
from application import views
from application.species import models

# Luodaan tietokantataulu
db.create_all()
