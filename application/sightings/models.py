from application import db
from application.models import Base, Info

class Sighting(Base, Info):
   
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

    def __init__(self, info):
        self.info = info
