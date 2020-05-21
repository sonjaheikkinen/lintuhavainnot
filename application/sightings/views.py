from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.sightings.models import Sighting
from application.sightings.forms import AddSighting



@app.route("/sightings", methods=["GET"])
def sightings_list():
    return render_template("sightings/list.html", sightings = Sighting.query.all())

@app.route("/sightings/new/", methods=["GET", "POST"])
@login_required
def sightings_add():

    if request.method == "POST":

        form = AddSighting(request.form) 

        if not form.validate():
            return render_template("sightings/new.html", form = form)

        sighting = Sighting(form.info.data)
        sighting.user_id = current_user.id
        
        db.session().add(sighting)
        db.session().commit()
  
        return redirect(url_for("sightings_list"))


    return render_template("sightings/new.html", form = AddSighting())



