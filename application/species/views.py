from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.species.models import Species
from application.species.forms import SpeciesCreationForm, SpeciesEditForm, SearchSpecies

from application.sightings.models import Sighting

conservInfo = {1: "Elinvoimainen, LC", 2: "Silmälläpidettävä, NT", 3: "Vaarantunut, VU", 
    4: "Erittäin uhanalainen, EN", 5: "Äärimmäisen uhanalainen, CR"}

@app.route("/species/search/<column>/<searchword>/<conservStatus>/", methods=["GET", "POST"])
def species_search(column, searchword, conservStatus):
    
    if request.method == "GET":
        return render_template("species/list.html",
         species = Species.search(column, searchword, conservStatus), conservInfo = conservInfo,
         form = SearchSpecies())

    form = SearchSpecies(request.form)
    if not form.validate():
        return render_template("species/list.html",
         species = Species.search(column, searchword, conservStatus), conservInfo = conservInfo,
         form = SearchSpecies())
    
    searchword = ""
    if form.searchword.data == "":
        searchword = "all"
    else:
        searchword = form.searchword.data

    return render_template("species/list.html",
         species = Species.search(form.column.data, searchword, form.conservStatus.data),
          conservInfo = conservInfo, form = SearchSpecies())

@app.route("/species/new/")
@login_required
def species_form():
    return render_template("species/new.html", form = SpeciesCreationForm())

@app.route("/species/edit/<species_id>/", methods=["GET", "POST"])
@login_required
def species_edit_information(species_id):

    species = Species.query.get(species_id)
    
    if request.method == "POST":

        form = SpeciesEditForm(request.form) 
        if not form.validate():
            return render_template("species/edit.html", species=species, form = form)

        species.name = form.name.data
        species.species = form.species.data
        species.sp_genus = form.sp_genus.data
        species.sp_family = form.sp_family.data
        species.sp_order = form.sp_order.data
        species.conserv_status = form.conserv_status.data
        species.info = form.info.data
        db.session().commit()
  
        return redirect(url_for("species_search", column="all", searchword="all", conservStatus=0))

    return render_template("species/edit.html", species=species, form = SpeciesEditForm(obj=species))

@app.route("/species/delete/<species_id>/", methods=["POST"])
@login_required
def species_delete(species_id):

     species = Species.query.get(species_id)
     db.session.query(Sighting).filter(Sighting.species_id == species_id).delete()
     db.session.delete(species)
     db.session.commit()
     return redirect(url_for("species_search", column="all", searchword="all", conservStatus=0))

@app.route("/species/", methods=["POST"])
@login_required
def species_create():

    form = SpeciesCreationForm(request.form) 
    if not form.validate():
        return render_template("species/new.html", form = form)

    species = Species(form.name.data, form.species.data,
     form.sp_genus.data, form.sp_family.data, form.sp_order.data,
     form.conserv_status.data, form.info.data)
    db.session().add(species)
    db.session().commit()
  
    return redirect(url_for("species_search", column="all", searchword="all", conservStatus=0))

@app.route("/species/show/<species_id>/")
def species_show(species_id):

    species = Species.query.get(species_id)

    nameparts = species.species.split(" ")
    nameLatin = ""
    if len(nameparts) == 3:
        nameLatin = nameparts[1] + " " + nameparts[2]
    else:
        nameLatin = nameparts[1]

    return render_template("species/info.html", species = species, conservInfo = conservInfo, nameLatin = nameLatin)
