from application import app, db
from flask import render_template, request
from application.species.models import Species

@app.route("/species/new/")
def species_form():
    return render_template("species/new.html")

@app.route("/species/", methods=["POST"])
def species_create():
    s = Species(request.form.get("name"))

    db.session().add(s)
    db.session().commit()
  
    return "Lintuja!"
