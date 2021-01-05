import sqlite3
import time
from string import ascii_letters
from random import choice, randrange

db = sqlite3.connect("indeksi.db")
db.isolation_level = None

c = db.cursor()

aika_alussa = time.time()

c.execute("CREATE TABLE Elokuvat (id INTEGER PRIMARY KEY, nimi TEXT, vuosi INTEGER)")

c.execute("BEGIN")
for i in range(1000001):
    nimi = ''.join(choice(ascii_letters) for k in range(11))
    vuosi = randrange(1900, 2001)
    c.execute("INSERT INTO Elokuvat (nimi, vuosi) VALUES (?,?)",[nimi,vuosi])
c.execute("COMMIT")

aika_kun_lisatty = time.time()

c.execute("CREATE INDEX idx_vuosi ON Elokuvat (vuosi)")

aika_kun_indeksoitu = time.time()

for i in range(1001):
    vuosi = randrange(1900, 2001)
    c.execute("SELECT COUNT(*) FROM Elokuvat WHERE vuosi=?",[vuosi])

aika_kun_kyselty = time.time()

print(f"Tietojen lisäämiseen käytetty aika: {aika_kun_lisatty-aika_alussa}")
print(f"Indeksointiin käytetty aika: {aika_kun_indeksoitu-aika_kun_lisatty}")
print(f"Tietojen kyselyyn käytetty aika: {aika_kun_kyselty-aika_kun_indeksoitu}")