from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SelectMultipleField, TextAreaField, validators, widgets
from application.species.models import Species

class AddSighting(FlaskForm):

    species = SelectField("Valitse havaittu laji:", coerce=int)
    place = StringField("Havaintopaikka:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    habitats = SelectMultipleField("Minkälainen ympäristö havaintopaikassa oli? (pidä Ctrl-näppäin pohjassa valitaksesi useampia vaihtoehtoja):", coerce=int)
    info = TextAreaField("Lisätietoja havainnosta:", render_kw={"rows": 10, "cols": 30})

    class Meta:
        csrf = False
    
class SearchSightings(FlaskForm):

    SpeciesFieldChoices = [("all", "Kaikki kentät"), ("name", "Lajinimi"),
     ("species", "Tieteellinen nimi"), ("sp_genus", "Suku"), ("sp_family", "Heimo"),
     ("sp_order", "Lahko"), ("info", "Lajikuvaus")]
    conservChoices2 = [("0", "Älä rajaa uhanalaisuuden perusteella"), ("1", "Elinvoimainen"),
     ("2", "Silmälläpidettävä"), ("3", "Vaarantunut"), ("4", "Erittäin uhanalainen"),
     ("5", "Äärimmäisen uhanalainen")]

    column = SelectField("Rajaa lajin perusteella -- kenttä", choices = SpeciesFieldChoices)
    searchword = StringField("Rajaa lajin perusteella -- hakusana:", [validators.Length(max=255, message="Kentän tulee olla enintään %(max)d merkkiä pitkä.")])	
    conservStatus = SelectField("Rajaa uhanalaisuuden perusteella:", choices=conservChoices2)
    place = StringField("Rajaa paikan perusteella:", [validators.Length(max=255, message="Kentän tulee olla enintään %(max)d merkkiä pitkä.")])
    habitat = StringField("Rajaa elinympäristön perusteella:", [validators.Length(max=255, message="Kentän tulee olla enintään %(max)d merkkiä pitkä.")])
    account = StringField("Hae tietyn käyttäjän tekemät havainnot:", [validators.Length(max=255, message="Kentän tulee olla enintään %(max)d merkkiä pitkä.")])      

    class Meta:
        csrf = False
    
    



