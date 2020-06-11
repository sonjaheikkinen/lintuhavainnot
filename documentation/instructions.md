# Käyttöohje

## Sovelluksen käyttöönotto

1. Siirry sovellukseen README:n linkitä "Sovellus Herokussa". Vaihtoehtoisesti voit asentaa sovelluksen [asennusohjeen](https://github.com/sonjaheikkinen/lintuhavainnot/blob/master/documentation/installation.md) mukaisesti omalle tietokoneellesi tai herokuun. Käynnistä sovellus asennusohjeiden mukaisesti. 

2. Rekisteröidy sovellukseen painamalla oikean ylänurkan linkkiä "Rekisteröidy". Kirjoita kenttiin oma nimesi, haluamasi käyttäjänimi, salasana, sekä mahdolliset haluamasi lisätiedot itsestäsi. 

3. Sovellus alustetaan niin, että kaikki uudet käyttäjät saavat admin-oikeudet. Mikäli haluat, että uudet käyttäjät rekisteröidään tavallisina käyttäjinä, muokkaa näitä asetuksia linkistä "Muokkaa käyttäjärooleja". Samalla sivulla voit halutessasi antaa tavalliselle käyttäjälle admin-oikeudet, tai poistaa ne. 

## Käyttäjätoiminnot

**Rekisteröityminen**

Rekisteröidy sovellukseen painamalla oikean ylänurkan linkkiä "Rekisteröidy". Kirjoita kenttiin oma nimesi, haluamasi käyttäjänimi, salasana, sekä mahdolliset haluamasi lisätiedot itsestäsi.

**Kirjautuminen**

Kirjaudu sovellukseen painamalla oikean ylänurkan linkkiä "Kirjaudu". Kirjoita kenttiin käyttäjätunnuksesi ja salasanasi.
Voit kirjautua ulos painamalla oikean ylänurkan linkkiä "Kirjaudu ulos"

**Käyttäasetukset**

Voit muokata nimeäsi, käyttäjätunnustasi, lisätietojasi ja salasanaasi oikean ylänurkan linkistä "Käyttäjäasetukset". Samasta linkistä pääset myös poistamaan käyttäjäsi. 

## Perustoiminnot

**Lintulajit**

Voit hakea tietoa lintulajeista välilehdeltä lajit. Etsi haluamasi laji listalta ja paina näytä tiedot, niin saat tarkempia tietoja kyseisestä lajista. Voit tarvittaessa hakea lajeja rajatusti sivun yläreunan lajihaun avulla. Lajeja voit hakea hakusanan ja uhanalaisuuden perusteella. Kun haet hakusanalla, voit joko hakea kyseisellä hakusanalla kaikista kentistä, tai valita pudotusvalikosta kentän, jonka perusteella haluat haun tehdä. Haku ei erottele pieniä ja isoja kirjaimia toisistaan, ja toimii myös sanan osilla. 

**Havainnot**

Voit tarkastella lintuhavaintoja linkistä havainnot. Havaintosivun yläreunalla on hakulomake, jonka avulla voit rajata näytettäviä havaintoja hyvinkin tarkasti. Voit myös tarkastella havainnoista muodostettuja tilastoja painamalla nappia "Näytä/piilota tilastot". 

Kirjaudu sisään ja paina nappia "Lisää havainto" lisätäksesi uusia lintuhavaintoja. Havainnon lisäämiseksi vaaditaan vähintään laji ja havaintopaikka, mutta halutessasi voit myös kirjoittaa havainnosta lisätietoja, sekä liittää havaintoon elinympäristön, jossa havaitsit lajin. 

## Admin-toiminnot

Admin-toimintoja pääset käyttämään yläpalkin linkistä Admin-työkalut. Osa toiminnoista on käytettävissä myös suoraan lajien ja havaintojen listaussivulta. 

**Lajit**

Admin-käyttäjänä voit lisätä uusia lajeja menemällä kohtaan Admin-työkalut>Lajit. Etsi sivulta lisäyslomake ja täytä kenttiin lajin tiedot. Tietoja pääset muokkaamaan hakemalla kyseisen lajin Lajit-sivulta ja painamallaa "Muokkaa tietoja". Napista "Poista", voit poistaa lajin. Huomaa, että toiminto poistaa myös kaikki kyseisestä lajista tehdyt havainnot. 

**Havainnot**

Voit poistaa ja muokata käyttäjien tekemiä havaintoja suoraan havaintojen listauksesta napeista "Muokkaa" ja "Poista". Havainnoista muokattavana on havaittu lintulaji, sekä havainnon lisätiedot. Mikäli haluat muokata havaintopaikkaa (esimerkiksi kirjoitusvirheen korjaamiseksi), mene kohtaan Admin-työkalut>Paikat ja elinympäristöt. 

**Käyttäjäroolit**

Linkistä "Muokkaa käyttäjärooleja" voit lisätä ja poistaa admin-oikeuksia käyttäjiltä, sekä valita rekisteröidäänkö uudet käyttäjät admin-käyttäjinä vai tavallisina käyttäjinä. Jos sovellus on esimerkiksi vain tutkimusryhmän sisäisessä käytössä, voi olla järkevää asettaa kaikki automaattisesti admin-käyttäjiksi. Julkiselle sovellukselle tätä ei kuitenkaan suositella.

**Paikat ja elinympäristöt**

Siirry tähän työkaluun yläpalkin linkeillä Admin-työalut>Paikat ja elinympäristöt. Paikka-listauksen napista "Muokkaa" voit muokata paikannimiä, sekä niihin liitettyjä elinympäristöjä. Voit myös poistaa paikan valitsemalla "Poista". Huomaa, että paikan poistaminen poistaa kaikki kyseisessä paikassa tehdyt havainnot.  Elinympäristölistauksesta voit muokata elinympäristöjen kirjoitusasua painamalla "Muokkaa" ja poistaa elinympäristön painamalla "Poista". Listauksen alta löydät myös lomakkeen uusien elinympäristöjen lisäämistä varten. Sekä paikka-, että elinympäristölistauksessa on käytettävissä hakutoiminnallisuus, joka ei erottele pieniä ja isoja kirjaimia toisistaan. 

**Tilastot**

Tilastosivulta (Admin-työkalut>Tilastot) voit tarkastella tietokannasta muodostettuja tilastoja. 



