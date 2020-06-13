# Käyttötapaukset

Alla lueteltuna sovelluksen käyttötapaukset. Jokaisen käyttötapauksen lopusta löytyvät siihen liittyvien SQL-kyselyiden numerot. SQL-kyselyt löytyvät numeroituina käyttötapausten alta. 

## Tavallinen käyttäjä

Käyttäjänä haluan saada tietoa Suomen lintulajeista. Lajien tiedot pitää pystyä listaamaan. Lintulajeista olisi hyvä olla tallennettuna vähintään kansankielinen nimi, kaksiosainen tieteellinen nimi ja lyhyt lajikuvaus. Muita tallennettavia tietoja voisivat olla esimerkiksi lajin tieteellinen luokittelu ja uhanalaisuus. *(1c)* **Valmis**

Käyttäjänä haluan hakea lintulajien tietoja myös rajatusti. Lajeja pitäisi pystyä rajaamaan ainakin nimen perusteella. Lisäksi talletettavista tiedoista riippuen lajeja voisi hakea esimerkiksi lajiryhmän tai uhanalaisuuden perusteella. *(1e, 1f, 1g, 1h, 1i)* **Valmis**

Käyttäjänä haluan lähettää tietokantaan omia lajihavaintojani. Havainnosta pitäisi tallettaa ainakin päivämäärä, paikka, ja havaittu laji. Lisäksi paikkoihin pitäisi pystyä liittämään niihin liittyviä elinympäristöjä. *(3a, 4a, 4b, 5a)* **Valmis**

Käyttäjänä haluan voida tarkastella omia havaintojani. Tätä varten tarvitaan jokin tapa tunnistaa käyttäjät, esimerkiksi kirjautumistoiminto. Omat havainnot pitää pystyä vähintään listaamaan. *(2a, 2b, 5d)* **Valmis**

Kirjautuneena käyttäjänä haluan voida muokata omia tietojani. *(2c, 2d, 2e)* **Valmis**

Käyttäjänä haluan tarkastella muiden tekemiä lintuhavaintoja. Havainnot pitäisi pystyä listaamaan ainakin lintulajin perusteella. Riippuen talletettavista attribuuteista havainnot olisi hyvä pystyä listaamaan myös esimerkiksi paikan, elinympäristön, linturyhmän ja uhanalaisuuden perusteella. *(5b, 5d)* **Valmis**

Käyttäjänä haluaisin tietää, mitä lintulajeja havaitaan eniten, ja mitä vähiten. *(6a)* **Valmis**

## Ylläpitäjä (esimerkiksi lintututkija)

*Tietokannan ylläpitäjänä haluan jo edellä mainittujen ominaisuuksien lisäksi seuraavat ominaisuudet:*

Ylläpitäjänä haluan voida lisätä, poistaa ja muokata lintulajien tietoja. *(1a, 1b, 1d, 5c)* **Valmis**

Ylläpitäjänä haluan voida tarkastella, muokata ja poistaa käyttäjien tekemiä lintuhavaintoja (esimerkiksi selvästi väärin tunnistettu laji). Havainnot pitää pystyä listaamaan yllä mainittujen ominaisuuksien lisäksi myös havaitsijan perusteella. *(5b, 5d, 5e, 5f)* **Valmis**

Ylläpitäjänä haluan, että sivusto on tietoturvallinen. Käyttäjien henkilötietojen ei tule näkyä muille kuin ylläpitäjille havaintoja listatessa. Salasanat tulee säilöä salattuna. *(Käyttötapaukseen ei liity sql-kyselyitä)* **Valmis**

Ylläpitäjänä haluan voida tarkastella, poistaa ja muokata paikkoja sekä niihin liitettyjä elinympäristöjä. Jokaisessa havaintopaikassa voi olla useampaa eri elinympäristöä, ja toisaalta sama elinympäristö voi liittyä useampaan eri paikkaan. Käyttäjät voivat kuitenkin havaintoja tehdessään tunnistaa elinympäristön väärin, joten korjausmahdollisuus tarvitaan. *(4c-4l, 5g)* **Valmis**

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
    SET name = ?, species = ?, sp_genus = ?, sp_family = ?, sp_order = ?, conserv_status = ?, info = ?
    WHERE id = ?;
```

**1c. Kaikkien lajien listaus**
```
SELECT * FROM Species;
```

**1d. Lajin poisto id:n perusteella**
```
DELETE FROM Species WHERE id = ?;
```

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
```
INSERT INTO Account (name, username, password, info) VALUES (?, ?, ?, ?);
```

**2b. Käyttäjän haku käyttäjänimen perusteella**
```
SELECT * FROM Account WHERE (username = ?);
```

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
```
DELETE FROM Account WHERE id = ?;
```

## Elinympäristöt

**3a. Elinympäristön lisäys**
```
INSERT INTO Habitat (name) VALUES (?);
```

## Paikat

**4a. Paikan lisäys**
```
INSERT INTO Place (name) VALUES (?);
```

**4b. Elinympäristöjen lisäys paikalle**
```
INSERT INTO PlaceHabitat (place_id, habitat_id) VALUES (?, ?);
```

**4c. Paikkojen ja elinympäristöjen listaus**
```
SELECT Place.id AS placeID, Place.name AS place,
 Habitat.name AS habitat FROM Place
  LEFT JOIN place_habitat ON place_habitat.place_id = Place.id
  LEFT JOIN Habitat ON Habitat.id = place_habitat.habitat_id;
```

**4d. Paikkojen ja elinympäristöjen haku paikannimen perusteella**
```
SELECT Place.id AS placeID, Place.name AS place,
 Habitat.name AS habitat FROM Place
  LEFT JOIN place_habitat ON place_habitat.place_id = Place.id
  LEFT JOIN Habitat ON Habitat.id = place_habitat.habitat_id
  WHERE place LIKE ?;
```

**4f. Paikkaan liitettyjen elinympäristöjen haku paikan id:n perusteella**
```
SELECT Habitat.id AS id FROM Habitat
 JOIN place_habitat ON place_habitat.habitat_id = Habitat.id
 JOIN Place ON Place.id = place_habitat.place_id
 WHERE Place.id = ?;
```

**4g. Paikka-elinympäristö-liitosten poisto paikan id:n perusteella**
```
DELETE FROM place_habitat 
 WHERE place_habitat.place_id = ?;
```

**4h. Paikan poisto id:n perusteella**
```
DELETE FROM Place WHERE Place.id = ?;
```

**4i. Paikan nimen muokkaus id:n perusteella**
```
UPDATE Place
 SET name = ?
 WHERE id = ?;
```
**4j. Paikka-elinympäristö-liitosten poisto elinympäristön id:n perusteella**
```
DELETE FROM place_habitat 
 WHERE place_habitat.habitat_id = ?;
```

**4k. Elinympäristön poisto id:n perusteella**
```
DELETE FROM Habitat WHERE Habitat.id = ?;
```

**4l. Elinympäristön nimen muokkaus id:n perusteella**
```
UPDATE Habitat
 SET name = ?
 WHERE id = ?;
```

## Havainnot

**5a. Havainnon lisäys**
```
INSERT INTO Sighting (info, account_id, species_id, place_id) VALUES (?, ?, ?, ?);
```

**5b. Havaintojen listaus**
```
SELECT * FROM Sighting;
```

**5c. Havaintojen poisto lintulajin perusteella**
```
DELETE FROM Sighting WHERE species_id = ?;
```

**5d. Havaintohaku**

Havaintohaun SQL-kysely rakennetaan ohjelmallisesti riippuen annetuista parametreistä. Koska mahdollisiä kysely-yhdistelmiä on todella monta, ei niitä kaikkia listata tässä erikseen. Alla valmis kysely, jossa on mukana kaikki mahdolliset rajausehdot. Mikäli jollekin rajausehdolle ei anneta parametria tai sen perusteella ei haeta, kyseinen rajausehto ei päädy toteutuneeseen kyselyyn. 

```
SELECT Sighting.*, Species.name AS species, Species.id AS speciesID,
 Place.name AS place, Habitat.name AS habitat,
 Account.username AS account FROM Sighting
  JOIN Species ON Sighting.species_id = Species.id
  JOIN Place ON Sighting.place_id = Place.id
  LEFT JOIN place_habitat ON place_habitat.place_id = Place.id
  LEFT JOIN Habitat ON place_habitat.habitat_id = Habitat.id
  LEFT JOIN Account ON Sighting.account_id = Account.id
  WHERE (upper(Species.name) LIKE ?
    OR upper(Species.species) LIKE ?
    OR upper(Species.sp_genus) LIKE ?
    OR upper(Species.sp_family) LIKE ?
    OR upper(Species.sp_order) LIKE ?
    OR upper(Species.info) LIKE ?)
  AND Species.conserv_status = ?
  AND upper(Place.name) LIKE ?
  AND upper(Habitat.name) LIKE ?
  AND upper(Account.username) LIKE ?
  ORDER BY Sighting.id;
```

**5e. Havainnon nimen ja kuvauksen muokkaus id:n perusteella**
```
UPDATE Sighting
  SET name = ?, info = ?
  WHERE id = ?;
```

**5f. Havainnon poisto id:n perusteella**
```
DELETE FROM Sighting WHERE id = ?;
```

**5g. Havainnon poisto paikka-id:n perusteella**
```
DELETE FROM Sighting WHERE place_id = ?;
```

## Useampien taulujen kyselyt

**6a. Eniten havaittujen lintulajien ja havaintojen määrän listaus**
```
SELECT Species.name, COUNT(*) AS count FROM Sighting
JOIN Species ON Sighting.species_id = Species.id
GROUP BY Species.id
ORDER BY count DESC
LIMIT 5;
```







