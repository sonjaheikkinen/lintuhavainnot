from application import db

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    species = db.Column(db.String(255), nullable=False)
    #sp_genus = db.Column(db.String(144), nullable=False)
    #sp_family = db.Column(db.String(144), nullable=False)
    #sp_order = db.Column(db.String(144), nullable=False)
    info = db.Column(db.Text, nullable=True)

    sightings = db.relationship("Sighting", backref='Species', lazy=True)

    #def __init__(self, name, species, sp_genus, sp_family, sp_order, description):
    def __init__(self, name, species, info):
        self.name = name
        self.species = species
        #self.sp_genus = sp_genus
        #self.sp_family = sp_family
        #self.sp_order = sp_order
        self.info = info
