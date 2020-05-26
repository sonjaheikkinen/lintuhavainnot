from application import app, db
from application.species.models import Species
from application.auth.models import User

# Lisataan lajeja
speciesText = open("application/files/species.txt", "r")
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
attributes = open("application/files/users.txt", "r").split(";")
user = User(attributes[0], attributes[1], attributes[2], attributes[3])
if not User.query.all():
    db.session.add(user)
    db.session.commit()
