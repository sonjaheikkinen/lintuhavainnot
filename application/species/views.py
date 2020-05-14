from application import app
from flask import render_template, request

@app.route("/species/new/")
def species_form():
    return render_template("species/new.html")

@app.route("/species/", methods=["POST"])
def species_create():
    print(request.form.get("name"))
  
    return "Lintuja!"
