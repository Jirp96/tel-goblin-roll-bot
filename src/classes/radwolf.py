import os
import random
import sqlite3

TEXT_POSITION = 1

class RadAdvice():
    advice_quotes = []
    
    def __init__(self) -> None:
        con = sqlite3.connect(os.environ["GOBLIN_DB"])
        cur = con.cursor()
        res = cur.execute("SELECT * FROM rad_advise;")
        self.advice_quotes.extend(res.fetchall())

    def advise(self) -> str:
        advise = random.choice(self.advice_quotes)
        
        return advise[TEXT_POSITION]