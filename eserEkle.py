from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

baglanti = sqlite3.connect("eserveri.db")
sorgu = baglanti.cursor()


def eserEkle():
    formVeri = (e1.get(), e2.get(), e3.get())
    sorgu.execute("INSERT INTO eserler VALUES(NULL,?,?,?)", formVeri)
    baglanti.commit()
    messagebox.showinfo(title="Katalog Bilgi", message="Eser başarıyla eklendi..!")
def formTemizle():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')

pencere = Tk()
pencere.title('Katalog: Eser Ekle')
pencere.geometry('300x200')
pencere.resizable = True
pencere['bg'] = '#FBE54E'

eserCercevesi = ttk.Frame(pencere, padding=10)
eserCercevesi.pack()

l1 = Label(eserCercevesi, text="Eser Adı")
l2 = Label(eserCercevesi, text="Eser Basım")
l3 = Label(eserCercevesi, text="Eser URL")
l4 = Label(eserCercevesi, text=":")
l5 = Label(eserCercevesi, text=":")
l6 = Label(eserCercevesi, text=":")
e1 = Entry(eserCercevesi, width=25)
e2 = Entry(eserCercevesi, width=25)
e3 = Entry(eserCercevesi, width=25)
b1 = Button(eserCercevesi, text="Yeni Eser Ekle", command=eserEkle)
b2 = Button(eserCercevesi, text="Temizle", command=formTemizle)

l1.grid(row=0, column=0, sticky=W, pady=2)
l4.grid(row=0, column=1, sticky=W, pady=2)
e1.grid(row=0, column=2, pady=2)
l2.grid(row=1, column=0, sticky=W, pady=2)
l5.grid(row=1, column=1, sticky=W, pady=2)
e2.grid(row=1, column=2, pady=2)
l3.grid(row=2, column=0, sticky=W, pady=2)
l6.grid(row=2, column=1, sticky=W, pady=2)
e3.grid(row=2, column=2, pady=2)
b1.grid(row=3, column=2, pady=2)
b2.grid(row=3, columnspan=2, pady=2)

pencere.mainloop()
