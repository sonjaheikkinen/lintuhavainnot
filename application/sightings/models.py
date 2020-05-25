from application import db

class Sighting(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    info = info = db.Column(db.Text, nullable=True)    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)
   


    def __init__(self, info):
        self.info = info
