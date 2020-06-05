from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.sightings.models import Sighting
from application.sightings.forms import AddSighting, SearchSightings

from application.species.models import Species
from application.auth.models import User
from application.places.models import Place, PlaceHabitat, Habitat

conservInfo = {0: "kaikki", 1: "Elinvoimainen, LC", 2: "Silmälläpidettävä, NT", 3: "Vaarantunut, VU", 
    4: "Erittäin uhanalainen, EN", 5: "Äärimmäisen uhanalainen, CR"}
columnInfo = {"all": "kaikki", "name": "lajinimi", "species": "tieteellinen nimi", "sp_genus": "suku", 
    "sp_family": "heimo", "sp_order": "lahko", "info": "lajikuvaus"}

@app.route("/sightings/search/<column>/<searchword>/<conservStatus>/<place>/<habitat>/<account>/", methods=["GET", "POST"])
def sightings_list(column, searchword, conservStatus, place, habitat, account):
    
    speciesWithMostSightings = Sighting.speciesWithMostSightings()
    speciesWithLeastSightings = Sighting.speciesWithLeastSightings()
    sightingsList = []
    form = ""
    searchResultString = ""

    if request.method == "POST":
        form = SearchSightings(request.form)
        column = form.column.data
        searchword = getSearchString(form.searchword.data, "all")
        conservStatus = form.conservStatus.data
        place = getSearchString(form.place.data, "all")
        habitat = getSearchString(form.habitat.data, "all")
        account = getSearchString(form.account.data, "all")
        sightingsList = Sighting.search(column, searchword, conservStatus, place, habitat, account)
        sightings = getSightingInformation(sightingsList)
    else:
        form = SearchSightings()
        sightingsList = Sighting.search(column, searchword, conservStatus, place, habitat, account)
        sightings = getSightingInformation(sightingsList)

    searchResultString = getSearchResultString(column, searchword, conservStatus, place, habitat, account)

    return render_template("sightings/list.html", sightings = sightings,
     speciesMost = speciesWithMostSightings, speciesLeast = speciesWithLeastSightings, form=form,
     searchResultString = searchResultString)


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
  
        return redirect(url_for("sightings_list", column="all", searchword="all", conservStatus="0",
         place="all", habitat="all", account="all"))

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
            if index == len(sightingInformation) - 1:
                sightings.append(sightingInformation)
        else:
            sightingInformation[2] = sightingInformation[2] + ", " + habitat
        
        if index == len(sightingsList) - 1:
                sightings.append(sightingInformation)
        
   
    return sightings

def getAccountString(sighting):
    if sighting.account_id == None:
        return "Poistunut käyttäjä"
    else:
        return sighting.account

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

def getSearchString(data, allString):
    if data == "" or data == "all":
        return allString
    else: 
        return data

def getSearchResultString(column, searchword, conservStatus, place, habitat, account):
    string = "Hakutulokset haulle kenttä: " + columnInfo[column] 
    string = string + ", hakusana: " + getSearchString(searchword, "kaikki")
    string = string + ", uhanalaisuusluokitus: " + conservInfo[int(conservStatus)]
    string = string + ", havaintopaikka: " + getSearchString(place, "kaikki")
    string = string + ", elinympäristö: " + getSearchString(habitat, "kaikki")
    string = string + ", käyttäjätunnus: " + getSearchString(account, "kaikki")
    return string




