<p align="center">
  <img src="https://i.imgur.com/ZHrVy1k.png">
</p>

# ANKIPYTHIA
Barebones flashcard app built on Tkinter and inspired by the official Anki app - https://apps.ankiweb.net/

- Create decks and add cards!
- Lightweight (The windows executable is only 8MB).
- Cross-platform (Any OS that can run Python 3).
- SQLite is used as the database to store decks and cards locally.

![Animation](https://github.com/1898Angelo/ankipythia/assets/123282394/a594b86a-a496-49e3-9dce-532fc7d5909f)

# TODO:
- Follow SOLID principles.
- Fix the time complexity of the sorting algorithm.
- Implement statistics tracking.

## DEPENDENCIES
```
customtkinter>=5.1.3
platformdirs>=2.6.2
```

- SQLite binaries are necessary to run the program. They are already included within the repository, but you can download them yourself from:
>https://www.sqlite.org/download.html

- On Linux, you might have to download Tkinter library packages separately.
>https://tecadmin.net/how-to-install-python-tkinter-on-linux/

## DATABASE STRUCTURE
The database follows a very simple star schema to avoid redundancies in the database:
- A dimension table _card_ is used to store the "front" and "back" of each card input into the program.
  - Furthermore, the table has a foreign key column _deck_id_ to relate multiple rows (cards) to each observation (deck name) in the fact table.
- A fact table _card_ is used to store the _deck name_ of each cards deck.

**DIMENSION TABLE**
```
CREATE TABLE "card" (
	"timestamp"	INTEGER NOT NULL, # To add timeseries analysis (and other functionalities) in the future.
	"deck_id"	INTEGER NOT NULL, # Foreign key column to avoid redundancies.
	"id"	INTEGER NOT NULL UNIQUE, 
	"front"	TEXT NOT NULL, # Front of each card.
	"back"	TEXT NOT NULL, # Back of each card.
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("deck_id") REFERENCES "deck_lookup"("id")
);
```
**FACT TABLE**
```
CREATE TABLE "deck" (
	"id"	INTEGER NOT NULL UNIQUE, # Primary key column referenced by card.
	"name"	TEXT NOT NULL UNIQUE, # Deck names are stored here.
	PRIMARY KEY("id" AUTOINCREMENT)
);
```

## HOW TO
### ... RUN IT ON WINDOWS
Download the executable from the releases section and run it! or if you prefer to run it from the source code, follow the steps below.

### ... RUN IT ON OTHER OPERATING SYSTEMS 
After installing the Python dependencies and SQLite binaries, clone or download the repository as a zip file; from the terminal, move into the directory and execute main.py.
```
(if cloning repo with git) git clone https://github.com/1898Angelo/ankipythia.git
cd ankipythia
main.py
```
### ... INSTALL PYTHON DEPENDENCIES
From the terminal set the cwd to the directory where you downloaded (cloned) the repo and run:
```
pip install -r requirements.txt
```
### ... DELETE DATABASE
Your decks and their respective cards are stored within a database in the current user's data directory:
- On windows
```
C:\Users\YourUserName\AppData\Local\Ankipythia
```
- On MacOS
```
/Users/YourUserName/Library/Application Support/Ankipythia
```
- On Linux
```
/home/YourUserName/.local/share/Ankipythia
```
