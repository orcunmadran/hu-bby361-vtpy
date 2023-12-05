import sqlite3

con = sqlite3.connect("data.sqlite3")
cur = con.cursor()

anahtar = input("Anahtar kelimeyi giriniz: ")

res = cur.execute(
    "SELECT * FROM books WHERE title LIKE('%{}%') OR author LIKE('%{}%') ORDER BY author DESC".format(anahtar,anahtar)
)
veriler = res.fetchall()
for satir in veriler:
    print(satir)