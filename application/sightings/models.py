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

    @staticmethod
    def speciesWithLeastSightings():
        
        stmt = text("SELECT Species.name, COUNT(*) AS count FROM Sighting"
                    " JOIN Species ON Sighting.species_id = Species.id"
                    " GROUP BY Species.id"
                    " ORDER BY count ASC"
                    " LIMIT 5")

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)
        return response

    @staticmethod
    def search(column, searchword, conservStatus, place, habitat, account):

        stmtString = Sighting.defineSelectAndJoins()
        stmt = Sighting.constructSearchStatement(stmtString, column, searchword, conservStatus, place, habitat, account)      
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)
        return response

    @staticmethod
    def defineSelectAndJoins():
        stmtString = "SELECT Sighting.*, Species.name AS species,"
        stmtString = stmtString + " Place.name AS place, Habitat.name AS habitat,"
        stmtString = stmtString + " Account.username AS account FROM Sighting"
        stmtString = stmtString + " JOIN Species ON Sighting.species_id = Species.id"
        stmtString = stmtString + " JOIN Place ON Sighting.place_id = Place.id"
        stmtString = stmtString + " LEFT JOIN place_habitat ON place_habitat.place_id = Place.id"
        stmtString = stmtString + " LEFT JOIN Habitat ON place_habitat.habitat_id = Habitat.id"
        stmtString = stmtString + " LEFT JOIN Account ON Sighting.account_id = Account.id"
        return stmtString
    
    @staticmethod
    def constructSearchStatement(stmtString, column, searchword, conservStatus, place, habitat, account):

        if not searchword == "all":
            searchword = "%" + searchword.upper() + "%"
            if not column == "all":
                stmtString = Sighting.searchFromColumn(column, searchword, stmtString)
            else:
                stmtString = Sighting.searchFromAllColumns(searchword, stmtString)
        
        if not conservStatus == "0":
            stmtString = Sighting.searchByConservStatus(conservStatus, stmtString)

        if not place == "all":
            place = "%" + place.upper() + "%"
            stmtString = Sighting.searchByPlace(place, stmtString)
        
        if not habitat == "all":
            habitat = "%" + habitat.upper() + "%"
            stmtString = Sighting.searchByHabitat(habitat, stmtString)
        
        if not account == "all":
            account = "%" + account.upper() + "%"
            stmtString = Sighting.searchByAccount(account, stmtString)
        
        stmtString = stmtString + " ORDER BY Sighting.id"
        stmt = text(stmtString).params(searchword = searchword, conservStatus = conservStatus,
         place = place, habitat = habitat, account = account)
        
        return stmt

    @staticmethod
    def searchFromColumn(column, searchword, stmtString):
        if column == "name":
            stmtString = stmtString + " WHERE upper(Species.name) LIKE :searchword"
        elif column == "species":
            stmtString = stmtString + " WHERE upper(Species.species) LIKE :searchword"
        elif column == "sp_genus":
            stmtString = stmtString + " WHERE upper(Species.sp_genus) LIKE :searchword"
        elif column == "sp_family":
            stmtString = stmtString + " WHERE upper(Species.sp_family) LIKE :searchword"
        elif column == "sp_order":
            stmtString = stmtString + " WHERE upper(Species.sp_order) LIKE :searchword"
        elif column == "info":
            stmtString = stmtString + " WHERE upper(Species.info) LIKE :searchword"
        return stmtString
    
    @staticmethod
    def searchFromAllColumns(searchword, stmtString):
        stmtString = stmtString + " WHERE (upper(Species.name) LIKE :searchword"
        stmtString = stmtString + " OR upper(Species.species) LIKE :searchword" 
        stmtString = stmtString + " OR upper(Species.sp_genus) LIKE :searchword"
        stmtString = stmtString + " OR upper(Species.sp_family) LIKE :searchword" 
        stmtString = stmtString + " OR upper(Species.sp_order) LIKE :searchword" 
        stmtString = stmtString + " OR upper(Species.info) LIKE :searchword)" 
        return stmtString
    
    @staticmethod
    def searchByConservStatus(conservStatus, stmtString):
        if "WHERE" in stmtString:
            stmtString = stmtString + " AND (Species.conserv_status = :conservStatus)"
        else:
            stmtString = stmtString + " WHERE (Species.conserv_status = :conservStatus)"
        return stmtString

    @staticmethod
    def searchByPlace(place, stmtString):
        if "WHERE" in stmtString:
            stmtString = stmtString + " AND (upper(Place.name) LIKE :place)"
        else:
            stmtString = stmtString + " WHERE (upper(Place.name) LIKE :place)"
        return stmtString
    
    @staticmethod
    def searchByHabitat(habitat, stmtString):
        if "WHERE" in stmtString:
            stmtString = stmtString + " AND (upper(Habitat.name) LIKE :habitat)"
        else:
            stmtString = stmtString + " WHERE (upper(Habitat.name) LIKE :habitat)"
        return stmtString
    
    @staticmethod
    def searchByAccount(account, stmtString):
        if "WHERE" in stmtString:
            stmtString = stmtString + " AND (upper(Account.username) LIKE :account)"
        else:
            stmtString = stmtString + " WHERE (upper(Account.username) LIKE :account)"
        return stmtString