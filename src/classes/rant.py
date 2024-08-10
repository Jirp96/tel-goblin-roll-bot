import os
import random
import sqlite3

TEXT_POSITION = 1

class Rant():
    rant_quotes = []
    
    def __init__(self, db) -> None:
        database_name = db
        
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM rant;")
        self.rant_quotes.extend(result.fetchall())

    def rant(self) -> str:
        rant_res = random.choice(self.rant_quotes)
        
        return rant_res[TEXT_POSITION]