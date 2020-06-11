# Lintuhavainnot
Tietokantasovellus, kesä 2020

## Projektikuvaus:

Lintuhavainnot on harjoitustyönä toteutettu tietokanta, johon kuka tahansa kirjautunut käyttäjä voi lähettää tietoa tekemistään lintuhavainnoista. Tietokannasta voi hakea tietoa ympäri suomen havaituista linnuista esimerkiksi havaintopaikan, uhanalaisuuden, elinympäristön tai lintulajin perusteella. Tietokannasta löytyy myös hieman tietoa ja kuvauksia itse lajeista, sekä niiden tieteellisestä luokittelusta. Ylläpitäjät voivat lisätä, poistaa ja muokata lähes kaikkea tietokannassa olevaa tietoa. Käyttäjät itse voivat muokata vain omia tietojaan. Lajien tiedot, sekä tietokantaan tehdyt havainnot ovat julkisesti näkyvillä kaikille. 

## Ohjeita

Sovellus alustetaan valmiilla testilinnuilla. Lisäksi Herokuun alustetaan valmiiksi kaksi testikäyttäjää: yksi tavallinen, ja yksi admin-käyttäjä. 

Kirjaudu admin-käyttäjälle tiedoilla: `tunnus: testAdmin, salasana: testAdmin`

Kirjaudu tavalliselle käyttäjälle tiedoilla: `tunnus: testi, salasana: testi`

Voit vapaasti lisätä, muokata ja poistaa käyttäjiä ja lintulajeja. Älä muokkaa annettuja testikäyttäjien kirjautumistietoja tai poista niitä. Kaikki uudet rekisteröidyt käyttäjät varustetaan tällä hetkellä admin-oikeuksin. Jos haluat luoda uusia tavallisia käyttäjiä, luo ensin uusi käyttäjä, ja poista sitten admin-oikeudet yläpalkin linkistä "Muokkaa käyttäjärooleja". 

## Dokumentaatio

[Sovellus herokussa](https://tsoha2020-lintuhavainnot.herokuapp.com/)

[Asennusohje](https://github.com/sonjaheikkinen/lintuhavainnot/blob/master/documentation/installation.md)

[Käyttöohje](https://github.com/sonjaheikkinen/lintuhavainnot/blob/master/documentation/instructions.md)

[Tietokantakaavio](https://github.com/sonjaheikkinen/lintuhavainnot/blob/master/documentation/lintuhavainnot_tietokantakaavio_12052020.png)
Projektin tietokanta on englanninkielinen, ja tietokantakaavio tullaan myöhemmin korjaamaan sitä vastaavaksi.

[Tietokannan tekstimuotoinen kuvaus](https://github.com/sonjaheikkinen/lintuhavainnot/blob/master/documentation/databaseDescription.md)

[Käyttötapaukset](https://github.com/sonjaheikkinen/lintuhavainnot/blob/master/documentation/usecases.md)








