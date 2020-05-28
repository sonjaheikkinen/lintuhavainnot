from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, validators

conservChoices = [(1, "Elinvoimainen"), (2, "Silmälläpidettävä"),
 (3, "Vaarantunut"), (4, "Erittäin uhanalainen"), (5, "Äärimmäisen uhanalainen")]

class SpeciesCreationForm(FlaskForm):
    name = StringField("Lajinimi, kansakielinen:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])	
    species = StringField("Lajinimi, tieteellinen kaksiosainen:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    sp_genus = StringField("Suku:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    sp_family = StringField("Heimo:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    sp_order = StringField("Lahko:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    conserv_status = SelectField("Uhanalaisuusluokitus:", choices=conservChoices, coerce=int)
    info = TextAreaField("Lajikuvaus:", render_kw={"rows": 10, "cols": 30})

    class Meta:
        csrf = False
 
class SpeciesEditForm(FlaskForm):
    name = StringField("Lajinimi, kansakielinen:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])	
    species = StringField("Lajinimi, tieteellinen kaksiosainen:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    sp_genus = StringField("Suku:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    sp_family = StringField("Heimo:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    sp_order = StringField("Lahko:", [validators.Length(min=1, max=255, message="Kentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä.")])
    conserv_status = SelectField("Uhanalaisuusluokitus:", choices=conservChoices, coerce=int)
    info = TextAreaField("Lajikuvaus:", render_kw={"rows": 10, "cols": 30})


    class Meta:
        csrf = False

class SearchSpecies(FlaskForm):

    fieldChoices = [("all", "Kaikki kentät"), ("name", "Lajinimi"),
     ("species", "Tieteellinen nimi"), ("sp_genus", "Suku"), ("sp_family", "Heimo"),
     ("sp_order", "Lahko"), ("info", "Lajikuvaus")]
    conservChoices2 = [("0", "Älä rajaa uhanalaisuuden perusteella"), ("1", "Elinvoimainen"),
     ("2", "Silmälläpidettävä"), ("3", "Vaarantunut"), ("4", "Erittäin uhanalainen"),
     ("5", "Äärimmäisen uhanalainen")]

    column = SelectField("Minkä kentän perusteella haetaan?", choices = fieldChoices)
    searchword = StringField("Hakusana (jätä tyhjäksi, jos et halua hakea hakusanan perusteella):", [validators.Length(max=255, message="Kentän tulee olla enintään %(max)d merkkiä pitkä.")])	
    conservStatus = SelectField("Uhanalaisuusluokitus:", choices=conservChoices2)

    class Meta:
        csrf = False

