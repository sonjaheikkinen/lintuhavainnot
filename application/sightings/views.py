from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.sightings.models import Sighting
from application.sightings.forms import AddSighting

from application.species.models import Species

@app.route("/sightings", methods=["GET"])
def sightings_list():
    return render_template("sightings/list.html", sightings = Sighting.query.all())

@app.route("/sightings/new/", methods=["GET", "POST"])
@login_required
def sightings_add():

    species = Species.query.all()
    choiceList = []
    for species in species:
        choiceList.append((species.id, species.name))

    if request.method == "POST":

        form = AddSighting(request.form) 
        form.species.choices = choiceList

        if not form.validate():
            return render_template("sightings/new.html", form = form)

        sighting = Sighting(form.info.data)
        sighting.account_id = current_user.id
        sighting.species_id = form.species.data
        
        db.session().add(sighting)
        db.session().commit()
  
        return redirect(url_for("sightings_list"))

    else:
    
        form = AddSighting()  
        form.species.choices = choiceList  

        return render_template("sightings/new.html", form = form)



