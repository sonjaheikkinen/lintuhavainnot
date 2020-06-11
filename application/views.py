from flask import render_template
from application import app, db, login_required
from application.statistics import Statistics

@app.route("/")
def index():
               
    return render_template("index.html")

@app.route("/statistics")
@login_required(role="ADMIN")
def statistics():
    speciesViewCount = Statistics.speciesViewCount()  
    speciesPerHabitat = Statistics.speciesPerHabitat()      
    return render_template("statistics.html", speciesViewCount = speciesViewCount, 
      speciesPerHabitat = speciesPerHabitat)

