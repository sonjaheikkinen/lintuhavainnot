from application import db
from application.species.models import Species


stmt = text("COPY species FROM 'application\species.txt'"
            " USING DELIMITERS ';' WITH NULL AS 'null'")
db.engine.execute(stmt)
