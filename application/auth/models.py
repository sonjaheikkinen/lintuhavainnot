from application import db
from application.models import Base, Name, Info

class User(Base, Name, Info):

    __tablename__ = "account"

    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    sightings = db.relationship("Sighting", backref='account', lazy=True)

    def __init__(self, name, username, password, info):
        self.name = name
        self.username = username
        self.password = password
        self.info = info
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
