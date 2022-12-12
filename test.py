import sqlite3

#Veritabanı ile bağlantının kurulması
con = sqlite3.connect("katalog.sqlite3")
cur = con.cursor()

#Sorgulama
res = cur.execute("SELECT * FROM eserler")

#Sorgulama Sonuçlarının görüntülenmesi
for eser in res.fetchall():
    print(eser)