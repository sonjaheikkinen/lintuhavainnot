from application import db

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    species = db.Column(db.String(144), nullable=False)
    spGenus = db.Column(db.String(144), nullable=False)
    spFamily = db.Column(db.String(144), nullable=False)
    spOrder = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=True)

    def __init__(self, name, species, spGenus, spFamily, spOrder, description):
        self.name = name
        self.species = species
        self.spGenus = spGenus
        self.spFamily = spFamily
        self.spOrder = spOrder
        self.description = description
