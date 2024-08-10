import os
import random
import sqlite3

TEXT_POSITION = 1

class RadAdvice():
    advice_quotes = []
    
    def __init__(self, db) -> None:
        database_name = db
        
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM rad_advise;")
        self.advice_quotes.extend(result.fetchall())

    def advise(self) -> str:
        advise = random.choice(self.advice_quotes)
        
        return advise[TEXT_POSITION]