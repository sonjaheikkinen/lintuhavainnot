from application import app, db
from application.species.models import Species

speciesText = open("application/species.txt", "r")
speciesList = []

for line in speciesText:
    attributes = line.split(";")
    speciesList.append(Species(attributes[0], attributes[1], attributes[2]))
    
speciesText.close()

if not Species.query.all():
    db.session.add_all(speciesList)
    db.session.commit()
