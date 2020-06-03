from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.sightings.models import Sighting
from application.sightings.forms import AddSighting

from application.species.models import Species
from application.auth.models import User
from application.places.models import Place, PlaceHabitat, Habitat

@app.route("/sightings/", methods=["GET"])
def sightings_list():

    speciesWithMostSightings = Sighting.speciesWithMostSightings()

    sightingsList = Sighting.query.all()
    sightings = getSightingInformation(sightingsList)

    return render_template("sightings/list.html", sightings = sightings,
     species = speciesWithMostSightings)

@app.route("/sightings/<account_id>", methods=["GET"])
@login_required
def sightings_listUserSightings(account_id):

    speciesWithMostSightings = Sighting.speciesWithMostSightings()

    sightingsList = db.session.query(Sighting).filter(Sighting.account_id == current_user.id)
    sightings = getSightingInformation(sightingsList)

    return render_template("sightings/list.html", sightings = sightings,
     species = speciesWithMostSightings)


@app.route("/sightings/new/", methods=["GET", "POST"])
@login_required
def sightings_add():

    speciesChoices = makeChoiceList(Species.query.all())
    habitatChoices = makeChoiceList(Habitat.query.all())

    if request.method == "POST":

        form = AddSighting(request.form) 
        form.species.choices = speciesChoices
        form.habitats.choices = habitatChoices

        if not form.validate():
            return render_template("sightings/new.html", form = form)

        sightingPlace = getPlaceId(form.place.data)
        addHabitats(sightingPlace, form.habitats.data)

        sighting = Sighting(form.info.data)
        sighting.account_id = current_user.id
        sighting.species_id = form.species.data
        sighting.place_id = sightingPlace

        db.session().add(sighting)
        db.session().commit()
  
        return redirect(url_for("sightings_list"))

    else:
    
        form = AddSighting()  
        form.species.choices = speciesChoices 
        form.habitats.choices = habitatChoices

        return render_template("sightings/new.html", form = form)

def makeChoiceList(items):
    choiceList = []
    for item in items:
        choiceList.append((item.id, item.name))
    return choiceList

def getSightingInformation(sightingsList):

    sightings = []

    for sighting in sightingsList:

        species = Species.query.get(sighting.species_id)
        account = getAccountString(sighting)
        place = db.session.query(Place).filter(sighting.place_id == Place.id).first()
        habitats = getHabitatString(place)
        placeHabitatString = place.name + habitats
        sightings.append([species.name, placeHabitatString, account, sighting.info])
   
    return sightings

def getAccountString(sighting):
    account = User.query.get(sighting.account_id)
    if account == None:
        account = "Poistunut käyttäjä"
    else:
        account = account.name
    return account

def getHabitatString(place):

    placeHabitats = db.session.query(PlaceHabitat).filter(PlaceHabitat.place_id == place.id).all()

    habitatIds = []
    for habitat in placeHabitats:
        habitatIds.append(habitat.habitat_id)

    habitatString = ""

    if habitatIds:
        habitatString = " ("
        for id in habitatIds:
            habitat = Habitat.query.get(id)
            habitatString = habitatString  + habitat.name + ", "      
        habitatString = habitatString[:-2] + ")"

    return habitatString

def getPlaceId(selectedPlace):

    placeFound = db.session.query(Place).filter(Place.name == selectedPlace).first()
    sightingPlace = ""

    if not placeFound:
        sightingPlace = Place(selectedPlace)
        db.session().add(sightingPlace)
        db.session().commit()
    else:
        sightingPlace = placeFound

    return sightingPlace.id
    

def addHabitats(placeId, selectedHabitats):
        
    placeHabitats = db.session.query(PlaceHabitat).filter(PlaceHabitat.place_id == placeId).all()
    idList = []
    for item in placeHabitats:
        idList.append(item.habitat_id)
        
    addList = []
    for habitat in selectedHabitats:
        if not habitat in idList:
            addList.append(PlaceHabitat(placeId, habitat))
    db.session.add_all(addList)
    db.session.commit()





