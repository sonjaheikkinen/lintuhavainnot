from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.sightings.models import Sighting
from application.sightings.forms import AddSighting, SearchSightings

from application.species.models import Species
from application.auth.models import User
from application.places.models import Place, PlaceHabitat, Habitat

@app.route("/sightings/search/<column>/<searchword>/<conservStatus>/", methods=["GET", "POST"])
def sightings_list(column, searchword, conservStatus):
    
    speciesWithMostSightings = Sighting.speciesWithMostSightings()
    sightingsList = []
    form = ""

    if request.method == "POST":
        form = SearchSightings(request.form)
        searchword = ""
        if form.searchword.data == "":
            searchword = "all"
        else: 
            searchword = form.searchword.data
        sightingsList = Sighting.search(form.column.data, searchword, form.conservStatus.data)
        sightings = getSightingInformation(sightingsList)
    else:
        form = SearchSightings()
        sightingsList = Sighting.search(column, searchword, conservStatus)
        sightings = getSightingInformation(sightingsList)

    return render_template("sightings/list.html", sightings = sightings,
     species = speciesWithMostSightings, form=form)


#@app.route("/sightings/<account_id>", methods=["GET"])
#@login_required
#def sightings_listUserSightings(account_id):

#   speciesWithMostSightings = Sighting.speciesWithMostSightings()

#    sightingsList = db.session.query(Sighting).filter(Sighting.account_id == current_user.id)
#    sightings = getSightingInformation(sightingsList)

#    return render_template("sightings/list.html", sightings = sightings,
#     species = speciesWithMostSightings)


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
  
        return redirect(url_for("sightings_list", column="all", searchword="all", conservStatus="0"))

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

    sightingInformation = []
    sightings = []

    for index, sighting in enumerate(sightingsList):

        species = sighting.species
        place = sighting.place
        habitat = sighting.habitat
        account = getAccountString(sighting)
        info = sighting.info
        
        if index == 0:
            sightingInformation = [species, place, habitat, account, info]
        elif (index > 0) and (sighting.id != sightingsList[index - 1].id):
            if sightingInformation[2] == None:
                sightingInformation[2] = "Elinympäristö tuntematon"
            sightings.append(sightingInformation)
            sightingInformation = [species, place, habitat, account, info]
        else:
            sightingInformation[2] = sightingInformation[2] + ", " + habitat
   
    return sightings

def getAccountString(sighting):
    if sighting.account_id == None:
        return "Poistunut käyttäjä"
    else:
        return sighting.account

def getHabitatString(place_id):

    placeHabitats = db.session.query(PlaceHabitat).filter(PlaceHabitat.place_id == place_id).all()

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





