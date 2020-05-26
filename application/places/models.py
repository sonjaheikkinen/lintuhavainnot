from application import db
from application.models import Base, Name


class Place(Base, Name):

    PlaceHabitat = db.relationship("PlaceHabitat", backref='place', lazy=True)

    def __init__(self, name):
        self.name = name


class PlaceHabitat(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)
    habitat_id = db.Column(db.Integer, db.ForeignKey('habitat.id'), nullable=False)
    

class Habitat(Base, Name):

    PlaceHabitat = db.relationship("PlaceHabitat", backref='habitat', lazy=True)

    def __init__(self, name):
        self.name = name
