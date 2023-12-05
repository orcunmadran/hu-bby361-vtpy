from tkinter import *
from  tkinter import ttk
import sqlite3

pencere  = Tk()
pencere.title('Katalog: Eserleri Listele')
pencere.geometry('700x370')
pencere.resizable = True
pencere['bg'] = '#FBE54E'

eserTabloCercevesi = ttk.Frame(pencere, padding=25)
eserTabloCercevesi.pack()

eserTablosu = ttk.Treeview(eserTabloCercevesi)

eserTablosu['columns'] = ('id', 'price', 'title', 'author', 'genre', 'rating')

eserTablosu.column("#0", width=0,  stretch=NO)
eserTablosu.column("id",anchor=CENTER, width=50)
eserTablosu.column("price",anchor=CENTER, width=25)
eserTablosu.column("title",anchor=CENTER, width=150)
eserTablosu.column("author",anchor=CENTER, width=150)
eserTablosu.column("genre",anchor=CENTER, width=125)
eserTablosu.column("rating",anchor=CENTER, width=100)

eserTablosu.heading("#0",text="",anchor=CENTER)
eserTablosu.heading("id",text="ID",anchor=CENTER)
eserTablosu.heading("price",text="Fiyat",anchor=CENTER)
eserTablosu.heading("title",text="Başlık",anchor=CENTER)
eserTablosu.heading("author",text="Yazar",anchor=CENTER)
eserTablosu.heading("genre",text="Kategori",anchor=CENTER)
eserTablosu.heading("rating",text="Değerlendirme",anchor=CENTER)

eserTablosu.pack()

baglanti = sqlite3.connect("data.sqlite3")
sorgu = baglanti.cursor()
sonuc = sorgu.execute("SELECT * FROM books")

for index, eser in enumerate(sonuc.fetchall()):
    eserTablosu.insert(parent='',index='end',iid=index,text='',
    values=(eser[0],eser[5],eser[1],eser[2],eser[3],eser[6]))

def aramaYap():
    anahtar = arama.get()
    aramaSonuc = sorgu.execute(
        "SELECT * FROM books WHERE title LIKE('%{}%') OR author LIKE('%{}%') OR genre LIKE('%{}%') ORDER BY title DESC".format(anahtar,
                                                                                                          anahtar, anahtar)
    )

    for row in eserTablosu.get_children():
        eserTablosu.delete(row)

    for index, eser in enumerate(sonuc.fetchall()):
        eserTablosu.insert(parent='', index='end', iid=index, text='',
                           values=(eser[0], eser[5], eser[1], eser[2], eser[3], eser[6]))

aramaBaslik = Label(eserTabloCercevesi, text="Arama:")
arama = Entry(eserTabloCercevesi, width=25)
ara = Button(eserTabloCercevesi, text="Arama Yap!", command=aramaYap)
aramaBaslik.pack()
arama.pack()
ara.pack()

pencere.mainloop()