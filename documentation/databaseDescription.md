# Tietokannan tekstimuotoinen kuvaus

## Create Table -lauseet:

### Species

```
CREATE TABLE species (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(255) NOT NULL, 
	info TEXT, 
	species VARCHAR(255) NOT NULL, 
	sp_genus VARCHAR(255) NOT NULL, 
	sp_family VARCHAR(255) NOT NULL, 
	sp_order VARCHAR(255) NOT NULL, 
	conserv_status INTEGER, 
	PRIMARY KEY (id)
)
```

### Account

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(255) NOT NULL, 
	info TEXT, 
	username VARCHAR(255) NOT NULL, 
	password VARCHAR(255) NOT NULL, 
	role VARCHAR(255) NOT NULL, 
	PRIMARY KEY (id)
)
```

### Place

```
CREATE TABLE place (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(255) NOT NULL, 
	PRIMARY KEY (id)
)
```

### Habitat

```
CREATE TABLE habitat (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(255) NOT NULL, 
	PRIMARY KEY (id)
)
```

### Sighting

```
CREATE TABLE sighting (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	info TEXT, 
	account_id INTEGER, 
	species_id INTEGER NOT NULL, 
	place_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(species_id) REFERENCES species (id), 
	FOREIGN KEY(place_id) REFERENCES place (id)

)
```

#### PlaceHabitat

```
CREATE TABLE place_habitat (
	id INTEGER NOT NULL, 
	place_id INTEGER NOT NULL, 
	habitat_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(place_id) REFERENCES place (id), 
	FOREIGN KEY(habitat_id) REFERENCES habitat (id)
)
```



