# Tietokannan tekstimuotoinen kuvaus

## Create Table -lauseet:

### Species

```CREATE TABLE species (
	id INTEGER NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	species VARCHAR(255) NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
)```

### Account

```CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(255) NOT NULL, 
	username VARCHAR(255) NOT NULL, 
	password VARCHAR(255) NOT NULL, 
	info TEXT, 
	PRIMARY KEY (id)
)```

### Sighting

```CREATE TABLE sighting (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	info TEXT, 
	account_id INTEGER, 
	species_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(species_id) REFERENCES species (id)
)```


