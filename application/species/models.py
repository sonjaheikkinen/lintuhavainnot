from application import db

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    species = db.Column(db.String(144), nullable=False)
    genus = db.Column(db.String(144), nullable=False)
    family = db.Column(db.String(144), nullable=False)
    order = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=True)

    def __init__(self, name, species, genus, family, order, description):
        self.name = name
        self.species = species
        self.genus = genus
        self.family = family
        self.order = order
        self.description = description
