# Lintuhavainnot
Tietokantasovellus, kesä 2020

[Tietokantakaavio](https://github.com/sonjaheikkinen/lintuhavainnot/blob/master/documentation/lintuhavainnot_tietokantakaavio_12052020.png)
Projektin tietokanta on englanninkielinen, ja tietokantakaavio tullaan myöhemmin korjaamaan sitä vastaavaksi.

[Tietokannan tekstimuotoinen kuvaus](https://github.com/sonjaheikkinen/lintuhavainnot/blob/master/documentation/databaseDescription.md)

[Käyttötapaukset](https://github.com/sonjaheikkinen/lintuhavainnot/blob/master/documentation/usecases.md)

[Sovellus herokussa](https://tsoha2020-lintuhavainnot.herokuapp.com/)

## Projektikuvaus:

Projektin tarkoitus on toimia havaintotietokantana, johon kuka tahansa (kirjautunut?) käyttäjä voi lähettää tietoa havaitsemistaan lintulajeista. Tietokannasta voisi sitten hakea tietoa ympäri suomen havaituista linnuista esimerkiksi paikkakunnan, ajankohdan, elinympäristön tai lintulajin perusteella. Työmäärästä riippuen havaintoja voisi ehkä ryhmitellä myös uhanalaisuuden tms. tietojen perusteella. Lajeista voisi myös tallettaa pieniä tietoiskuja. Ylläpitäjät voivat poistaa ja muokata havaintoja, sekä nähdä käyttäjien tietoja ja heidän tekemänsä havainnot. Käyttäjät itse voivat nähdä vain omat tietonsa, sekä yleisellä tasolla muut havainnot. Käyttäjät eivät voi tehdä muokkauksia tietokantaan (mutta voivat lähettää korjausehdotuksia?). 

## Ohjeita

Sovellus alustetaan valmiilla testilinnuilla. Lisäksi Herokuun alustetaan valmiiksi kaksi testikäyttäjää: yksi tavallinen, ja yksi admin-käyttäjä. 

Kirjaudu admin-käyttäjälle tiedoilla: `tunnus: testAdmin, salasana: testAdmin`

Kirjaudu tavalliselle käyttäjälle tiedoilla: `tunnus: testi, salasana: testi`

Voit vapaasti lisätä, muokata ja poistaa käyttäjiä ja lintulajeja. Älä muokkaa annettuja testikäyttäjien kirjautumistietoja tai poista niitä. Kaikki uudet rekisteröidyt käyttäjät varustetaan tällä hetkellä admin-oikeuksin. Jos haluat luoda uusia tavallisia käyttäjiä, luo ensin uusi käyttäjä, ja poista sitten admin-oikeudet yläpalkin linkistä "Muokkaa käyttäjärooleja". 







