import os
import random
import sqlite3

TEXT_POSITION = 1

class Rant():
    rant_quotes = []
    
    def __init__(self) -> None:
        con = sqlite3.connect(os.environ["GOBLIN_DB"])
        cur = con.cursor()
        res = cur.execute("SELECT * FROM rant;")
        self.rant_quotes.extend(res.fetchall())

    def rant(self) -> str:
        rant_res = random.choice(self.rant_quotes)
        
        return rant_res[TEXT_POSITION]