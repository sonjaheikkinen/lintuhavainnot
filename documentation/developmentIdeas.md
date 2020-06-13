# Jatkokehitysideoita

## Kaikkien talletettavien tietojen hyödyntäminen

### Päivämäärät

Kaikille tietokantaan meneville tietokohteille talletetaan luomis- ja muokkauspäivämäärät. Näitä ei toistaiseksi hyödynnetä missään (käyttäjälistausta lukuunottamatta). Monia niistä voisi kuitenkin hyödyntää etenkin admin-työkalujen puolella. Ylläpitäjät voisivat esimerkiksi säännöllisesti tarkistaa ja päivittää sellaiset lintulajien kuvaukset, joita ei ole pitkään aikaan muokattu. 

### Kuvaukset

Monille tietokohteille talletetaan kuvaus. Lajin ja havainnon kuvaukset ovat jo käytössä, mutta käyttäjän kuvaus on pääosin turha. Sitä voisi hyödyntää esimerkiksi lisäämällä jokaiselle käyttäjälle julkisen profiilisivun, jossa he voisivat halutessaan kertoa jotain itsestään ja lintuharrastuksestaan. 

## Muita mahdollisia talletettavia tietoja

### Lajit

Lintulajeista voisi nykyisten tietojen lisäksi tallettaa esimerkiksi kuvan, levinneisyysluvun tai -kartan, tiedon mahdollisesta rauhoitusajasta, pesintäajan, tuntomerkit, ääninauhoitteen jne. Tietysti näitä tietoja voisi myös vain kirjoittaa vapaamuotoisesti kuvaukseen, jos asiat haluaa pitää yksinkertaisina.

### Käyttäjät

Käyttäjistä voisi tallettaa enemmän henkilötietoja, esimerkiksi sähköpostiosoitteen. Näin ylläpitäjät voisivat tarvittaessa kysyä käyttäjiltä lisätietoja johonkin havaintoon liittyen. Toisaalta jonkin viestinvaihtokanava sovelluksen sisäisesti ajaisi saman asian. Käyttäjätiedot auttaisivat myös arvioimaan onko havainnossa mainittu lintulaji tunnistettu oikein (useita havaintoja tehneet tunnistavat lajit todennäköisemmin oikein).

### Paikat ja elinympäristöt

Havaintopaikalle voisi tallettaa nimen lisäksi tarkemmat koordinaatin. Lisäksi paikka voisi muutenkin olla tarkemmin määritelty, kuin vain yksinäinen merkkijono. Erilliset kentään tarvittaisiin ainakin Kaupungille/Kunnalle, Kaupunginosalle/Kylälle/Paikkakunnalle ja aikaisemmin mainituille koordinaateille. Sekä paikoista, että elinympäristöistä voisi myös tallettaa sanalliset kuvaukset, jolloin myös luontoa tuntemattomat osaisivat paremmin valita havaintoon liitettävän elinympäristön oikein. 

## Hakutoimintojen parantaminen

### Lajihaku

Lintuja voi tällä hetkellä hakea uhanalaisuuden, yhden kentän, tai kaikkien kenttien perusteella. Tähän voisi toteuttaa tarkennetun haun, jossa jokaiselle kentälle voitaisiin antaa erillinen hakusana. Lajeille voitaisiin asettaa myös avainsanoja (esim. vesilinnut, pikkulinnut) joiden avulla myös tieteellisiä lajiryhmiä tuntemattoman olisi helpompi löytää haluamansa laji. Jonkinlainen lajinavigointi esimerkiksi lajiryhmien perusteella voisi myös auttaa ongelmaan. 

### Havaintohaku

Koska havaintohakuun kuuluu myös lajin perusteella hakeminen, niin tähän pätevät samat huomiot kuin yllä. Havaintoja olisi hyvä pystyä hakemaan myös päivämäärän, kuukauden, vuodenajan ja vuoden perusteella. 

## Käyttäjäryhmät ja havaintojen vahvistus

Havainnoilla pitäisi olla tieto, onko havainto vahvistettu, jotta käyttäjät tietäisivät mitkä havainnot ovat todennäköisesti luotettavasti oikein tunnistettuja. Tätä varten tarvitaan jonkinlainen admin-työkalu, jolla vahvistaminen on helppoa myös suuremmilla havaintomäärillä (kaikkea ei tarvitse vahvistaa yksitellen, vaan voitaisiin esimerkiksi asettaa, että kaikki tavanomaisissa ympäristöissä havaitut talitiaiset yms. peruslinnut vahvistetaan automaattisesti, ja toisaalta harvinaisten lintujen kohdalla ylläpitäjille voisi tulla jonkinlainen tarkistuskehotus). 

Sovellukseen voisi myös lisätä tätä työtaakkaa helpottamaan erillisen lintuharrastajat-käyttäjäryhmän. Tämän statuksen saisivat tunnetut pitkäaikaiset lintuharrastajat. Lintuharrastajilla olisi oikeus vahvistaa muiden käyttäjien tekemiä havaintoja. 

### Superadmin

Tällä hetkellä kaikilla admin-käyttäjillä on oikeus jakaa ja poistaa adminoikeuksia mielivaltaisesti. Olisi hyvä, jos sovelluksen omistajalla/haltijalla olisi oma superadmin-status. Vain tällä käyttäjällä olisi oikeus muokata toisten käyttäjien admin-oikeuksia. 

## Tilastotiedot

Tilastosivulle voisi lisätä erilaisia työkaluja, joilla ylläpitäjät voisivat laskea erilaisia tilastollisia tunnuslukuja aineistosta itse antamillaan parametreilla, sekä tulostaa erilaisia id-listoja tarkempaa tilastollista analyysia varten. 





