from application import db

class Sighting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    info = info = db.Column(db.Text, nullable=True)


    def __init__(self, info):
        self.info = info