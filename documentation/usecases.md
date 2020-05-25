# Käyttötapaukset

Alla lueteltuna sovelluksen käyttötapaukset. Jokaisen käyttötapauksen lopusta löytyvät siihen liittyvien SQL-kyselyiden numerot. SQL-kyselyt löytyvät numeroituina käyttötapausten alta. 

## Tavallinen käyttäjä

Käyttäjänä haluan saada tietoa Suomen lintulajeista. Lajien tiedot pitää pystyä listaamaan. Lintulajeista olisi hyvä olla tallennettuna vähintään kansankielinen nimi, kaksiosainen tieteellinen nimi ja lyhyt lajikuvaus. Muita tallennettavia tietoja voisivat olla esimerkiksi lajin tieteellinen luokittelu, levinneisyys ja uhanalaisuus. *(1c)*

Käyttäjänä haluan hakea lintulajien tietoja myös rajatusti. Lajeja pitäisi pystyä rajaamaan ainakin nimen perusteella. Lisäksi talletettavista tiedoista riippuen lajeja voisi hakea esimerkiksi lajiryhmän tai uhanalaisuuden perusteella. 

Käyttäjänä haluan lähettää tietokantaan omia lajihavaintojani. Havainnosta pitäisi tallettaa ainakin päivämäärä, paikka, ja havaittu laji. *(3a)*

Käyttäjänä haluan voida tarkastella omia havaintojani. Tätä varten tarvitaan jokin tapa tunnistaa käyttäjät, esimerkiksi kirjautumistoiminto. Omat havainnot pitää pystyä vähintään listaamaan. *(2a, 2b)*

Kirjautuneena käyttäjänä haluan voida muokata omia tietojani, esimerkiksi yhteystietoja. *(2c, 2d, 2e)*

Käyttäjänä haluan tarkastella muiden tekemiä lintuhavaintoja. Havainnot pitäisi pystyä listaamaan ainakin lintulajin perusteella. Riippuen talletettavista attribuuteista havainnot olisi hyvä pystyä listaamaan myös esimerkiksi paikan, elinympäristön, linturyhmän ja uhanalaisuuden perusteella. *(3b)*

## Ylläpitäjä (esimerkiksi lintututkija)

*Tietokannan ylläpitäjänä haluan jo edellä mainittujen ominaisuuksien lisäksi seuraavat ominaisuudet:*

Ylläpitäjänä haluan voida lisätä, poistaa ja muokata lintulajien tietoja. *(1a, 1b, 1d, 3c)*

Ylläpitäjänä haluan voida tarkastella, muokata ja poistaa käyttäjien tekemiä lintuhavaintoja (esimerkiksi selvästi väärin tunnistettu laji). Havainnot pitää pystyä listaamaan yllä mainittujen ominaisuuksien lisäksi myös havaitsijan perusteella. *(3b)*

Ylläpitäjänä haluan tavallisten laji- ja havaintolistausten lisäksi mahdollisuuden hakea samoilla tiedoilla id-listoja sekä nimi-id-taulukon tilastollisessa tutkimuksessa käytettäväksi.

Ylläpitäjänä haluan pystyä vahvistamaan havaintoja. Näin muut käyttäjät voivat esimerkiksi harvinaisten lajien kohdalla tietää, että kyseinen laji todella on havaittu, eikä vain väärin tunnistettu. Vahvistamista tehdään harkiten, jos samasta lajista on esimerkiksi useita havaintoja, tai havainto on tullut tunnetulta lintuharrastajalta.

Ylläpitäjänä haluan, että sivusto on tietoturvallinen. Käyttäjien henkilötietojen ei tule näkyä muille kuin ylläpitäjille havaintoja listatessa. Salasanat tulee säilöä salattuna.

Ylläpitäjänä haluan voida tarkastella, poistaa ja muokata paikkoihin liitettyjä elinympäristöjä. Jokaisessa havaintopaikassa voi olla useampaa eri elinympäristöä, ja toisaalta sama elinympäristö voi liittyä useampaan eri paikkaan. Käyttäjät voivat kuitenkin havaintoja tehdessään tunnistaa elinympäristön väärin, joten korjausmahdollisuus tarvitaan. 

# Käyttötapauksiin liittyvät SQL-kyselyt

## Lajit 

**1a. Lajin lisäys**

`INSERT INTO Species (name, species, description) VALUES (?, ?, ?);`

**1b. Lajin muokkaus id:n perusteella**

```
UPDATE Species
    SET name = ?, species = ?, description = ?
    WHERE id = ?;
```

**1c. Kaikkien lajien listaus**

`SELECT * FROM Species;`

**1d. Lajin poisto id:n perusteella**

`DELETE FROM Species WHERE id = ?;`

## Käyttäjät

**2a. Uuden käyttäjän lisäys**

`INSERT INTO Account (name, username, password, info) VALUES (?, ?, ?);`

**2b. Käyttäjän haku käyttäjänimen perusteella**

`SELECT * FROM Account WHERE (username = ?);`

**2c. Käyttäjän tietojen muokkaus id:n perusteella**

```
UPDATE Account
    SET name = ?, username = ?, info = ?
    WHERE id = ?;
```

**2d. Käyttäjän salasanan vaihto id:n perusteella**

```
UPDATE Account
    SET password = ?
    WHERE id = ?;
```

**2e. Käyttäjän poisto id:n perusteella**

`DELETE FROM Account WHERE id = ?;`

##Havainnot

**3a. Havainnon lisäys**

`INSERT INTO Sighting (info, account_id, species_id) VALUES (3?, ?, ?);`

**3b. Havaintojen listaus**

`SELECT * FROM Sighting;`

**3c. Havaintojen poisto lintulajin perusteella**

`DELETE FROM Sighting WHERE species_id = ?;`







