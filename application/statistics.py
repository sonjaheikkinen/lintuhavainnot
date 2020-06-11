from application import db
from application.species.models import Species
from application.sightings.models import Sighting
from application.places.models import Place, PlaceHabitat, Habitat
from sqlalchemy.sql import text

class Statistics:

    @staticmethod
    def speciesViewCount():
        stmt = text("SELECT Species.id AS id, Species.name AS name, Species.species AS species,"
                    " COUNT(Sighting.id) AS viewCount FROM Species"
                    " LEFT JOIN Sighting ON Sighting.species_id = Species.id"
                    " GROUP BY Species.id"
                    " ORDER BY viewCount DESC")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)
        return response

    @staticmethod
    def speciesPerHabitat():
        stmt = text("SELECT Habitat.name AS habitat, COUNT(Species.id) AS speciesCount FROM Habitat"
                    " LEFT JOIN place_habitat ON place_habitat.habitat_id = Habitat.id"
                    " LEFT JOIN Place ON Place.id = place_habitat.place_id"
                    " LEFT JOIN Sighting ON Sighting.place_id = Place.id"
                    " LEFT JOIN Species ON Species.id = Sighting.species_id"
                    " GROUP BY habitat"
                    " ORDER BY speciesCount DESC")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)
        return response

