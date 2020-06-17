from application import db
from application.models import Base, Name
from sqlalchemy.sql import text


class Place(Base, Name):

    PlaceHabitat = db.relationship("PlaceHabitat", backref='place', lazy=True)
    Sighting = db.relationship("Sighting", backref='place', lazy=True)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def getPlaceAndHabitats(searchword):

        stmtString = "SELECT Place.id AS place_id, Place.name AS place, Habitat.name AS habitat FROM Place"
        stmtString = stmtString + " LEFT JOIN place_habitat ON place_habitat.place_id = Place.id"
        stmtString = stmtString + " LEFT JOIN Habitat ON Habitat.id = place_habitat.habitat_id"
       
        if not searchword == "all":
            searchword = "%" + searchword + "%"
            stmtString = stmtString + " WHERE place LIKE :searchword"
    
        stmt = text(stmtString).params(searchword = searchword)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
           response.append(row)
        return response

    @staticmethod
    def getHabitatIds(place_id):
        stmt = text("SELECT Habitat.id AS id FROM Habitat"
                    " JOIN place_habitat ON place_habitat.habitat_id = Habitat.id"
                    " JOIN Place ON Place.id = place_habitat.place_id"
                    " WHERE Place.id = :placeID").params(placeID = place_id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
           response.append(row[0])
        return response

    

    


class PlaceHabitat(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)
    habitat_id = db.Column(db.Integer, db.ForeignKey('habitat.id'), nullable=False)

    def __init__(self, place_id, habitat_id):
        self.place_id = place_id
        self.habitat_id = habitat_id
    

class Habitat(Base, Name):

    PlaceHabitat = db.relationship("PlaceHabitat", backref='habitat', lazy=True)

    def __init__(self, name):
        self.name = name
