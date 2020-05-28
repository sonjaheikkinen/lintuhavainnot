from application import db
from application.models import Base, Info
from sqlalchemy.sql import text

class Sighting(Base, Info):
   
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

    def __init__(self, info):
        self.info = info

    @staticmethod
    def speciesWithMostSightings():
        
        stmt = text("SELECT Species.name, COUNT(*) AS count FROM Sighting"
                    " JOIN Species ON Sighting.species_id = Species.id"
                    " GROUP BY Species.id"
                    " ORDER BY count DESC"
                    " LIMIT 5")

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)
        return response


    


