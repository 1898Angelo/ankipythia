import sqlite3
from platformdirs import user_data_dir
from os import makedirs
from os.path import join

class API(object):
    __appname__ = "Ankipythia"
    __appauthor__ = "1898Angelo"
    __dbname__ = "ankipythia.db"
    __dir__ = user_data_dir(__appname__, appauthor=False)
    __db__ = join(__dir__, __dbname__)

    def __init__(self, *args, **kwargs):
        pass
        
    def query(self, query, parameters=None) -> sqlite3.Cursor:
        #print(f"Query: {query}\nParameters: {parameters}")
        if parameters is None:
            parameters = []
        with sqlite3.connect(self.__db__) as connection:
            cursor = connection.cursor()
            result = cursor.execute(query, parameters)
            connection.commit()
        return result
    
    def exists(self, deck: str) -> bool:
        query = "SELECT 1 FROM deck_lookup WHERE deck_name == (?)"
        parameters = (deck,)
        if self.query(query, parameters).fetchone():
            return True
        return False
    
    @classmethod
    def __create_tables__(cls):
        card = """
        CREATE TABLE if not exists "card" (
	        "timestamp"	INTEGER NOT NULL,
	        "deck_id"	INTEGER NOT NULL,
	        "id"	INTEGER NOT NULL UNIQUE,
	        "front"	TEXT NOT NULL,
	        "back"	TEXT NOT NULL,
        FOREIGN KEY("deck_id") REFERENCES "deck_lookup"("id"),
	    PRIMARY KEY("id" AUTOINCREMENT)
        );
        """

        lookup_table = """
        CREATE TABLE if not exists "deck_lookup" (
	        "id"	INTEGER NOT NULL UNIQUE,
	        "deck_name"	TEXT NOT NULL UNIQUE,
	    PRIMARY KEY("id" AUTOINCREMENT)
        );
        """

        cls.query(cls, query=card)
        cls.query(cls, query=lookup_table)
    
    @classmethod
    def __db_dir__(cls):
        return makedirs(cls.__dir__, exist_ok=True)
    
    def __enter_deck__(self, deck: str):
        deck.title()
        query = "INSERT INTO deck_lookup(deck_name) VALUES (?)"
        parameters = (deck,)
        return self.query(query, parameters)
