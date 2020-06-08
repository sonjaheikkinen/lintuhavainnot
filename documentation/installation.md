# Sovelluksen asennus ja käyttöönotto

## Sovelluksen asennus paikallisesti

1. Lataa sovellus GitHubista osoitteesta https://github.com/sonjaheikkinen/lintuhavainnot. Tämä onnistuu painamalla repositorion oikeassa laidassa olevaa vihreää nappia "Clone or download", ja valitsemalla avautuvasta pudotusvalikosta "Download ZIP".

2. Etsi ladattu tiedosto koneeltasi (useimmiten ladatut tiedostot päätyvät kansioon "Downloads"/"Ladatut tiedostot"), ja siirrä se haluamaasi kansioon. Klikkaa sitten tiedostoa hiiren kakkospainikkeella, ja valitse avautuvasta valikosta vaihtoehto "Pura tänne"/"Extract here". Kansiossa pitäisi nyt olla alikansio nimeltä lintuhavainnot-master. Voit halutessasi poistaa zip-tiedoston. 

*Sovellus asennetaan ja käynnistetään komentoriviltä. Tämä ohje on kirjoitettu Linux-käyttöjärjestelmälle. Jos käytät jotain toista käyttöjärjestelmää, selvitä oman käyttöjärjestelmäsi vastaavat komennot.*

3. Avaa tietokoneesi komentoliittymä, ja navigoi kansioon lintuhavainnot-master. Navigointi onnistuu esimerkiksi komennoilla `ls`, joka näyttää tämänhetkisen kansiosi alikansiot, sekä `cd kansionnimi`, jolla pääset liikkuumaan seuraavaan kansioon. 

4. Luo kansioon Python-virtuaaliympäristö komennolla `python3 -m venv venv`.

5. Aktivoi virtuaaliympäristö komennolla `source venv/bin/activate`. Komentorivin vasemmassa laidassa pitäisi nyt näkyä teksti (venv). 

5. Asenna sovelluksen tarvitsemat riippuvuudet komennolla `pip install -r requirements.txt`. Mikäli komento aiheuttaa varoituksen **Cache entry deserialization failed, entry ignored**, päivitä pip komennolla `pip install --upgrade pip`, ja aja ensimmäinen komento sen jälkeen uudestaan.

6. Kun haluat käyttää sovellusta, varmista, että olet kansiossa lintuhavainnot-master, aktivoi virtuaaliympäristö komennolla `source venv/bin/activate`, mikäli sitä ei ole jo tehty (aktivointi poistuu aina sulkiessasi komentoliittymän), ja käynnistä sovellus komennolla `python run.py`. Sovellus löytyy nyt internet-selaimella osoitteesta *http://localhost:5000/*. Voit pysäyttää sovelluksen näppäinyhdistelmällä `Ctrl + c` tai sulkemalla komentoliittymän. 


## Sovelluksen asennus Herokuun

1. Asenna sovellus ensin paikallisesti (ks. ylläoleva ohje, vaiheet 1-5). Varmista, että käytettävissäsi on tunnukset [Herokuun](https://www.heroku.com/). 

2. Asenna tarvittaessa [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) ja [konfiguroi](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) se. 

2. Asenna tarvittaessa [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), jotta voit käyttää Herokua komentoriviltä. Kirjaudu Herokuun komennolla `heroku login`. 

3. Luo tarvittaessa tunnus [GitHubiin](https://github.com/), ja luo uusi repositorio valitsemalla oikean ylänurkan pudotusvalikosta "Your repositories" ja painamalla vihreää nappia "New". Varmista, että kohta "Initialize this repository with a README" ei ole valittuna. 

*Suorita seuraavat vaiheet kansiossa lintuhavainnot-master*

4. Lisää sovellukselle versionhallinta komennolla `git init`. 

5. Yhdistä sovelluksesi GitHubin repositorioon komennolla `git remote add origin git@github.com:githubkäyttäjätunnus/repositorionnimi`.

6. Lisää tiedostot GitHubiin suorittamalla komennot `git add .`, `git commit -m "Initial commit"` ja `git push -u origin master`. 

7. Luo Heroku-sovellus komennolla `heroku create sovellusnimi`. Voit sijoittaa sovellusnimeksi minkä tahansa merkkijonon (esimerkiksi lintuhavainnot-sovellus), tai jättää sen tyhjäksi, jolloin Heroku antaa sovellukselle satunnaisen nimen. 

8. Yhdistetään heroku paikalliseen versionhallintaan komennolla `git remote add heroku https://git.heroku.com/sovellusnimi.git`.

8. Siirrä projekti Herokuun komennoilla `git add .`, `git commit -m "Initial commit"` ja `git push heroku master`.

9. Sovellus toimii nyt osoitteessa https://sovellusnimi.herokuapp.com/
