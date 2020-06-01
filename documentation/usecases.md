# Käyttötapaukset

Alla lueteltuna sovelluksen käyttötapaukset. Jokaisen käyttötapauksen lopusta löytyvät siihen liittyvien SQL-kyselyiden numerot. SQL-kyselyt löytyvät numeroituina käyttötapausten alta. 

## Tavallinen käyttäjä

Käyttäjänä haluan saada tietoa Suomen lintulajeista. Lajien tiedot pitää pystyä listaamaan. Lintulajeista olisi hyvä olla tallennettuna vähintään kansankielinen nimi, kaksiosainen tieteellinen nimi ja lyhyt lajikuvaus. Muita tallennettavia tietoja voisivat olla esimerkiksi lajin tieteellinen luokittelu, levinneisyys ja uhanalaisuus. *(1c)*

Käyttäjänä haluan hakea lintulajien tietoja myös rajatusti. Lajeja pitäisi pystyä rajaamaan ainakin nimen perusteella. Lisäksi talletettavista tiedoista riippuen lajeja voisi hakea esimerkiksi lajiryhmän tai uhanalaisuuden perusteella. *(1e, 1f, 1g, 1h, 1i)*

Käyttäjänä haluan lähettää tietokantaan omia lajihavaintojani. Havainnosta pitäisi tallettaa ainakin päivämäärä, paikka, ja havaittu laji. Lisäksi paikkoihin pitäisi pystyä liittämään niihin liittyviä elinympäristöjä. *(3a, 4a, 4b, 5a)*

Käyttäjänä haluan voida tarkastella omia havaintojani. Tätä varten tarvitaan jokin tapa tunnistaa käyttäjät, esimerkiksi kirjautumistoiminto. Omat havainnot pitää pystyä vähintään listaamaan. *(2a, 2b)*

Kirjautuneena käyttäjänä haluan voida muokata omia tietojani, esimerkiksi yhteystietoja. *(2c, 2d, 2e)*

Käyttäjänä haluan tarkastella muiden tekemiä lintuhavaintoja. Havainnot pitäisi pystyä listaamaan ainakin lintulajin perusteella. Riippuen talletettavista attribuuteista havainnot olisi hyvä pystyä listaamaan myös esimerkiksi paikan, elinympäristön, linturyhmän ja uhanalaisuuden perusteella. *(5b)*

Käyttäjänä haluaisin tietää, mitä lintulajeja havaitaan eniten. *(6a)*

## Ylläpitäjä (esimerkiksi lintututkija)

*Tietokannan ylläpitäjänä haluan jo edellä mainittujen ominaisuuksien lisäksi seuraavat ominaisuudet:*

Ylläpitäjänä haluan voida lisätä, poistaa ja muokata lintulajien tietoja. *(1a, 1b, 1d, 5c)*

Ylläpitäjänä haluan voida tarkastella, muokata ja poistaa käyttäjien tekemiä lintuhavaintoja (esimerkiksi selvästi väärin tunnistettu laji). Havainnot pitää pystyä listaamaan yllä mainittujen ominaisuuksien lisäksi myös havaitsijan perusteella. *(5b)*

Ylläpitäjänä haluan tavallisten laji- ja havaintolistausten lisäksi mahdollisuuden hakea samoilla tiedoilla id-listoja sekä nimi-id-taulukon tilastollisessa tutkimuksessa käytettäväksi.

Ylläpitäjänä haluan pystyä vahvistamaan havaintoja. Näin muut käyttäjät voivat esimerkiksi harvinaisten lajien kohdalla tietää, että kyseinen laji todella on havaittu, eikä vain väärin tunnistettu. Vahvistamista tehdään harkiten, jos samasta lajista on esimerkiksi useita havaintoja, tai havainto on tullut tunnetulta lintuharrastajalta.

Ylläpitäjänä haluan, että sivusto on tietoturvallinen. Käyttäjien henkilötietojen ei tule näkyä muille kuin ylläpitäjille havaintoja listatessa. Salasanat tulee säilöä salattuna.

Ylläpitäjänä haluan voida tarkastella, poistaa ja muokata paikkoihin liitettyjä elinympäristöjä. Jokaisessa havaintopaikassa voi olla useampaa eri elinympäristöä, ja toisaalta sama elinympäristö voi liittyä useampaan eri paikkaan. Käyttäjät voivat kuitenkin havaintoja tehdessään tunnistaa elinympäristön väärin, joten korjausmahdollisuus tarvitaan. 

# Käyttötapauksiin liittyvät SQL-kyselyt

## Lajit 

**1a. Lajin lisäys**

```
INSERT INTO Species (name, species, sp_genus, sp_family, sp_order, conserv_status, info) 
VALUES (?, ?, ?, ?, ?, ?, ?);
```

**1b. Lajin muokkaus id:n perusteella**

```
UPDATE Species
    SET name = ?, species = ?, description = ?, sp_genus = ?, sp_family = ?, sp_order = ?, conserv_status = ?, info = ?
    WHERE id = ?;
```

**1c. Kaikkien lajien listaus**

`SELECT * FROM Species;`

**1d. Lajin poisto id:n perusteella**

`DELETE FROM Species WHERE id = ?;`

**1e. Lajihaku yhden kentän ja hakusanan perusteella**
```
SELECT * FROM Species
WHERE upper(kentännimi) LIKE ?;
```

**1f. Lajihaku kaikkien kentän ja hakusanan perusteella**
```
SELECT * FROM Species
WHERE (upper(name) LIKE ?
 OR upper(species) LIKE ?
 OR upper(sp_genus) LIKE ?
 OR upper(sp_family) LIKE ? 
 OR upper(sp_order) LIKE ? 
 OR upper(info) LIKE ?);
```

**1g. Lajihaku uhanalaisuuden perusteella**
```
SELECT * FROM Species
WHERE conserv_status = ?;
```

**1h. Lajihaku yhden kentän ja hakusanan sekä uhanalaisuuden perusteella**
```
SELECT * FROM Species
WHERE upper(kentännimi) LIKE ?
AND conserv_status = ?;
```

**1i. Lajihaku kaikista kentistä hakusanalla ja rajaus uhanalaisuuden perusteella**
```
SELECT * FROM Species
WHERE (upper(name) LIKE ?
 OR upper(species) LIKE ?
 OR upper(sp_genus) LIKE ?
 OR upper(sp_family) LIKE ? 
 OR upper(sp_order) LIKE ? 
 OR upper(info) LIKE ?)
 AND conserv_status = ?;
```

## Käyttäjät

**2a. Uuden käyttäjän lisäys**

`INSERT INTO Account (name, username, password, info) VALUES (?, ?, ?, ?);`

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

## Elinympäristöt

**3a. Elinympäristön lisäys**

`INSERT INTO Habitat (name) VALUES (?);`

## Paikat

**4a. Paikan lisäys**

`INSERT INTO Place (name) VALUES (?);`

**4b. Elinympäristöjen lisäys paikalle**

`INSERT INTO PlaceHabitat (place_id, habitat_id) VALUES (?, ?);`

## Havainnot

**5a. Havainnon lisäys**

`INSERT INTO Sighting (info, account_id, species_id, place_id) VALUES (?, ?, ?, ?);`

**5b. Havaintojen listaus**

`SELECT * FROM Sighting;`

**5c. Havaintojen poisto lintulajin perusteella**

`DELETE FROM Sighting WHERE species_id = ?;`

## Useampien taulujen kyselyt

**6a. Eniten havaittujen lintulajien ja havaintojen määrän listaus

```
SELECT Species.name, COUNT(*) AS count FROM Sighting
JOIN Species ON Sighting.species_id = Species.id
GROUP BY Species.id
ORDER BY count DESC
LIMIT 5
```







