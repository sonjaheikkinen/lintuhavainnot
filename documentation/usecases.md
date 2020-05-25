# Käyttötapaukset

## Tavallinen käyttäjä

Käyttäjänä haluan saada tietoa Suomen lintulajeista. Lajien tiedot pitää pystyä listaamaan. Lintulajeista olisi hyvä olla tallennettuna vähintään kansankielinen nimi, kaksiosainen tieteellinen nimi ja lyhyt lajikuvaus. Muita tallennettavia tietoja voisivat olla esimerkiksi lajin tieteellinen luokittelu, levinneisyys ja uhanalaisuus. 

Käyttäjänä haluan hakea lintulajien tietoja myös rajatusti. Lajeja pitäisi pystyä rajaamaan ainakin nimen perusteella. Lisäksi talletettavista tiedoista riippuen lajeja voisi hakea esimerkiksi lajiryhmän tai uhanalaisuuden perusteella. 

Käyttäjänä haluan lähettää tietokantaan omia lajihavaintojani. Havainnosta pitäisi tallettaa ainakin päivämäärä, paikka, ja havaittu laji.

Käyttäjänä haluan voida tarkastella omia havaintojani. Tätä varten tarvitaan jokin tapa tunnistaa käyttäjät, esimerkiksi kirjautumistoiminto. Omat havainnot pitää pystyä vähintään listaamaan.

Kirjautuneena käyttäjänä haluan voida muokata omia tietojani, esimerkiksi yhteystietoja.

Käyttäjänä haluan tarkastella muiden tekemiä lintuhavaintoja. Havainnot pitäisi pystyä listaamaan ainakin lintulajin perusteella. Riippuen talletettavista attribuuteista havainnot olisi hyvä pystyä listaamaan myös esimerkiksi paikan, elinympäristön, linturyhmän ja uhanalaisuuden perusteella.

## Ylläpitäjä (esimerkiksi lintututkija)

*Tietokannan ylläpitäjänä haluan jo edellä mainittujen ominaisuuksien lisäksi seuraavat ominaisuudet:*

Ylläpitäjänä haluan voida lisätä, poistaa ja muokata lintulajien tietoja.

Ylläpitäjänä haluan voida tarkastella, muokata ja poistaa käyttäjien tekemiä lintuhavaintoja (esimerkiksi selvästi väärin tunnistettu laji). Havainnot pitää pystyä listaamaan yllä mainittujen ominaisuuksien lisäksi myös havaitsijan perusteella.

Ylläpitäjänä haluan tavallisten laji- ja havaintolistausten lisäksi mahdollisuuden hakea samoilla tiedoilla id-listoja sekä nimi-id-taulukon tilastollisessa tutkimuksessa käytettäväksi.

Ylläpitäjänä haluan pystyä vahvistamaan havaintoja. Näin muut käyttäjät voivat esimerkiksi harvinaisten lajien kohdalla tietää, että kyseinen laji todella on havaittu, eikä vain väärin tunnistettu. Vahvistamista tehdään harkiten, jos samasta lajista on esimerkiksi useita havaintoja, tai havainto on tullut tunnetulta lintuharrastajalta.

Ylläpitäjänä haluan, että sivusto on tietoturvallinen. Käyttäjien henkilötietojen ei tule näkyä muille kuin ylläpitäjille havaintoja listatessa. Salasanat tulee säilöä salattuna.

Ylläpitäjänä haluan voida tarkastella, poistaa ja muokata paikkoihin liitettyjä elinympäristöjä. Jokaisessa havaintopaikassa voi olla useampaa eri elinympäristöä, ja toisaalta sama elinympäristö voi liittyä useampaan eri paikkaan. Käyttäjät voivat kuitenkin havaintoja tehdessään tunnistaa elinympäristön väärin, joten korjausmahdollisuus tarvitaan. 

# Käyttötapauksiin liittyvät SQL-kyselyt

**Lajin lisäys**


**Lajien listaus**
`SELECT * FROM Species;`







