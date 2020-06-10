from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application import app, db, login_required
from application.places.forms import Search, EditPlace, EditHabitat
from application.places.models import Place, PlaceHabitat, Habitat
from application.sightings.models import Sighting

@app.route("/places/search/<searchword>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def places_search(searchword):

    form = Search()

    if request.method == "POST":
        form = Search(request.form)
        searchword = form.name.data

    places = []
    if (searchword == None) or (searchword == "") or (searchword=="all"):
        places = Place.getPlaceAndHabitats("all")
    else:
        places = Place.getPlaceAndHabitats(searchword)

    places = getPlaceInformation(places)

    return render_template("places/list.html", places = places, habitats = Habitat.query.all(), form = form)

@app.route("/places/delete/<place_id>/", methods=["POST"])
@login_required(role="ADMIN")
def places_delete(place_id):

    db.session.query(PlaceHabitat).filter(PlaceHabitat.place_id == place_id).delete()
    db.session.query(Sighting).filter(Sighting.place_id == place_id).delete()
    db.session.query(Place).filter(Place.id == place_id).delete()
    db.session.commit()
    return redirect(url_for("places_search", searchword = "all"))

@app.route("/places/edit/<place_id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def places_edit(place_id):

    place = Place.query.get(place_id)

    if request.method == "GET":
        form = EditPlace()
        form.name.default = place.name
        form.habitat.choices = makeChoiceList(Habitat.query.all())
        form.habitat.default = Place.getHabitatIds(place_id)
        form.process()
        return render_template("places/editPlace.html", place_id = place_id, form = form)
    else:
        form = EditPlace(request.form)
        place.name = form.name.data
        editPlaceHabitats(place, form.habitat.data)
        db.session.commit()
        return redirect(url_for("places_search", searchword = "all"))        

@app.route("/habitats/edit/<habitat_id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def habitats_edit(habitat_id):

    habitat = Habitat.query.get(habitat_id)

    if request.method == "GET":
        form = EditHabitat()
        form.name.default = habitat.name
        form.process()
        return render_template("places/editHabitat.html", habitat_id = habitat_id, form = form)
    else:
        form = EditHabitat(request.form)
        habitat.name = form.name.data
        db.session.commit()
        return redirect(url_for("places_search", searchword = "all"))

@app.route("/habitats/delete/<habitat_id>/", methods=["POST"])
@login_required(role="ADMIN")
def habitats_delete(habitat_id):

    db.session.query(PlaceHabitat).filter(PlaceHabitat.habitat_id == habitat_id).delete()
    db.session.query(Place).filter(Habitat.id == habitat_id).delete()
    db.session.commit()
    return redirect(url_for("places_search", searchword = "all"))


def getPlaceInformation(places):

    placeList = []
    placeInfo = {}
    
    for index, place in enumerate(places):
        if index == 0:
            placeInfo = {"id": place.placeID, "place": place.place, "habitats": place.habitat}
        elif (index > 0) and (place.place != places[index - 1].place):
            if placeInfo["habitats"] == None:
                placeInfo["habitats"] = "Elinympäristö tuntematon"
            placeList.append(placeInfo)
            placeInfo = {"id": place.placeID, "place": place.place, "habitats": place.habitat}
        else:
            placeInfo["habitats"] = placeInfo["habitats"] + ", " + place.habitat
        if index == len(places) - 1:
            placeList.append(placeInfo)

    return placeList

def makeChoiceList(items):
    choiceList = []
    for item in items:
        choiceList.append((item.id, item.name))
    return choiceList

def editPlaceHabitats(place, habitatIds):
    db.session.query(PlaceHabitat).filter(PlaceHabitat.place_id == place.id).delete()
    PlaceHabitatList = []
    for habitat_id in habitatIds:
        PlaceHabitatList.append(PlaceHabitat(place.id, habitat_id))
    db.session.add_all(PlaceHabitatList)
    db.session.commit()


    


