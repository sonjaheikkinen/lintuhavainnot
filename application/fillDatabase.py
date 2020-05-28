from application import app, db
from application.species.models import Species
from application.places.models import Habitat
from application.auth.models import User

# Lisataan lajeja
speciesText = open("application/files/species.txt", "r")
speciesList = []

for line in speciesText:
    attributes = line.split(";")
    species = Species(attributes[0], attributes[1],
     attributes[2], attributes[3], attributes[4], 
     int(attributes[5]), attributes[6])
    speciesList.append(species)   
    
speciesText.close()

if not Species.query.all():
    db.session.add_all(speciesList)
    db.session.commit()

# Lisataan elinymparistoja
habitatText = open("application/files/habitats.txt", "r")
habitatList = []

for line in habitatText:
    habitatList.append(Habitat(line.strip()))   
    
habitatText.close()

if not Habitat.query.all():
    db.session.add_all(habitatList)
    db.session.commit()

# Lisataan testikayttaja
#userText = open("application/files/users.txt", "r")
#attributes = userText.readline().split(";")
#user = User(attributes[0], attributes[1], attributes[2], attributes[3])
#if not User.query.all():
#    db.session.add(user)
#    db.session.commit()
