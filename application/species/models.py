from application import db
from application.models import Base, Name, Info
from sqlalchemy.sql import text

class Species(Base, Name, Info):
    species = db.Column(db.String(255), nullable=False)
    sp_genus = db.Column(db.String(255), nullable=False)
    sp_family = db.Column(db.String(255), nullable=False)
    sp_order = db.Column(db.String(255), nullable=False)
    conserv_status = db.Column(db.Integer)

    sightings = db.relationship("Sighting", backref='Species', lazy=True)

    def __init__(self, name, species, sp_genus, sp_family, sp_order, conserv_status, info):
        self.name = name
        self.species = species
        self.sp_genus = sp_genus
        self.sp_family = sp_family
        self.sp_order = sp_order
        self.conserv_status = conserv_status
        self.info = info

    @staticmethod
    def search(column, searchword, conservStatus):

        stmtString = "SELECT * FROM Species"

        if not searchword == "all":
            if not column == "all":
                stmtString = Species.searchFromColumn(column, searchword, stmtString)
            else:
                stmtString = Species.searchFromAllColumns(searchword, stmtString)
        
        if not conservStatus == "0":
            stmtString = Species.searchByConservStatus(conservStatus, stmtString)

        stmt = text(stmtString)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)
        return response

    @staticmethod
    def searchFromColumn(column, searchword, stmtString):
        stmtString = stmtString + " WHERE (" + column + " LIKE '%" +  searchword + "%')"
        return stmtString
    
    @staticmethod
    def searchFromAllColumns(searchword, stmtString):
        stmtString = stmtString + " WHERE (name LIKE '%" +  searchword + "%'"
        stmtString = stmtString + " OR species LIKE '%" + searchword + "%'" 
        stmtString = stmtString + " OR sp_genus LIKE '%" + searchword + "%'" 
        stmtString = stmtString + " OR sp_family LIKE '%" + searchword + "%'" 
        stmtString = stmtString + " OR sp_order LIKE '%" + searchword + "%'" 
        stmtString = stmtString + " OR info LIKE '%" + searchword + "%')" 
        return stmtString
    
    @staticmethod
    def searchByConservStatus(conservStatus, stmtString):
        if "WHERE" in stmtString:
            stmtString = stmtString + " AND conserv_status = " + conservStatus
        else:
            stmtString = stmtString + " WHERE conserv_status = " + conservStatus
        return stmtString
