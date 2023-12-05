import sqlite3

con = sqlite3.connect("data.sqlite3")
cur = con.cursor()

kat = cur.execute("SELECT DISTINCT UPPER(SUBSTR(genre, 1, 1)) || SUBSTR(genre, 2) FROM books ORDER BY genre")
katListe = kat.fetchall()

print("Kategori listesi:")
for count, katSatir in enumerate(katListe):
    print(str(count+1) +" - "+ katSatir[0])

kategoriID = int(input("Lütfen kategori ID giriniz: "))

if kategoriID == 1:
    secilenKategori = "fiction"
elif kategoriID == 2:
    secilenKategori = "mystery"
elif kategoriID == 3:
    secilenKategori = "non-fiction"
elif kategoriID == 4:
    secilenKategori = "romance"
elif kategoriID == 5:
    secilenKategori = "sci-fi"
else:
    print("Seçim Hatalı..!")

res = cur.execute(
    "SELECT * FROM books WHERE genre = '{}'".format(secilenKategori)
)

veriler = res.fetchall()
for satir in veriler:
    print(satir)
print("Toplam kayıt sayısı " + str(len(veriler)))