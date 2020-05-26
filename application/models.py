from application import db

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

class Name(db.Model):

    __abstract__ = True
  
    name = db.Column(db.String(255), nullable=False)


class Info(db.Model):

    __abstract__ = True
  
    info = db.Column(db.Text, nullable=True)