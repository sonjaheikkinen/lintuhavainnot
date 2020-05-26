from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.sightings.models import Sighting
from application.sightings.forms import AddSighting

from application.species.models import Species
from application.auth.models import User
from application.places.models import Place, PlaceHabitat, Habitat

@app.route("/sightings", methods=["GET"])
def sightings_list():

    sightingsList = Sighting.query.all()
    sightings = []
    for sighting in sightingsList:
        species = Species.query.get(sighting.species_id)
        account = User.query.get(sighting.account_id)
        if account == None:
            account = "Poistunut käyttäjä"
        else:
            account = account.name

        sightings.append([species.name, sighting.info, account])

    return render_template("sightings/list.html", sightings = sightings)

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

        sighting = Sighting(form.info.data)
        sighting.account_id = current_user.id
        sighting.species_id = form.species.data
        selectedPlace = form.place.data
        selectedHabitats = form.habitats.data

        placeFound = db.session.query(Place).filter(Place.name == selectedPlace).first()
        newPlace = ""

        if not placeFound:
            newPlace = Place(selectedPlace)
            db.session().add(newPlace)
            db.session().commit()
        else:
            newPlace = placeFound
        
        placeHabitats = db.session.query(PlaceHabitat).filter(PlaceHabitat.place_id == newPlace.id).all()
        idList = []
        for item in placeHabitats:
            idList.append(item.id)
        
        addList = []
        for habitat in selectedHabitats:
            if not habitat in idList:
                addList.append(PlaceHabitat(newPlace.id, habitat))
        db.session.add_all(addList)

        sighting.place_id = newPlace.id

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
  



