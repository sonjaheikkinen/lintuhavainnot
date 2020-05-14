from application import app, db
from flask import render_template, request
from application.species.models import Species

@app.route("/species", methods=["GET"])
def species_index():
    return render_template("species/list.html", species = Species.query.all())

@app.route("/species/new/")
def species_form():
    return render_template("species/new.html")

@app.route("/species/", methods=["POST"])
def species_create():
    s = Species(request.form.get("name"), request.form.get("species"), 
    request.form.get("description"))

    db.session().add(s)
    db.session().commit()
  
    return "Lintuja!"
