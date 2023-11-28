import sqlite3
con = sqlite3.connect("veri.sqlite3")
cur = con.cursor()
res = cur.execute("SELECT * from eser LIMIT 5")
veriler = res.fetchall()
print(veriler[0])