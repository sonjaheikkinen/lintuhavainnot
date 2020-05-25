from application import app, db
from application.species.models import Species
from application.auth.models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# Lisataan lajeja
speciesText = open("application/species.txt", "r")
speciesList = []

for line in speciesText:
    attributes = line.split(";")
    species = Species(attributes[0], attributes[1], attributes[2])
    speciesList.append(species)   
    
speciesText.close()

if not Species.query.all():
    db.session.add_all(speciesList)
    db.session.commit()

# Lisataan testikayttaja
hashedPassword = bcrypt.generate_password_hash("testi").decode('utf-8')
testUser = User("testi", "testi", hashedPassword, "Tämä on testikäyttäjä")
userFound = User.query.filter_by(username="testi").first()
if userFound:
     if not bcrypt.check_password_hash(userFound.password, "testi"):
         db.session.add(testUser)
         db.session.commit()
else: 
    db.session.add(testUser)
    db.session.commit()
