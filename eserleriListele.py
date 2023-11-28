from tkinter import *
from  tkinter import ttk
import sqlite3

baglanti = sqlite3.connect("eserveri.db")
sorgu = baglanti.cursor()
sonuc = sorgu.execute("SELECT * FROM eserler")

pencere  = Tk()
pencere.title('Katalog: Eserleri Listele')
pencere.geometry('800x300')
pencere.resizable = True
pencere['bg'] = '#FBE54E'

eserTabloCercevesi = ttk.Frame(pencere, padding=25)
eserTabloCercevesi.pack()

eserTablosu = ttk.Treeview(eserTabloCercevesi)

eserTablosu['columns'] = ('eserID', 'eserAdi', 'eserBasim', 'eserURL')

eserTablosu.column("#0", width=0,  stretch=NO)
eserTablosu.column("eserID",anchor=CENTER, width=50)
eserTablosu.column("eserAdi",anchor=CENTER,width=250)
eserTablosu.column("eserBasim",anchor=CENTER,width=75)
eserTablosu.column("eserURL",anchor=CENTER,width=250)

eserTablosu.heading("#0",text="",anchor=CENTER)
eserTablosu.heading("eserID",text="Eser ID",anchor=CENTER)
eserTablosu.heading("eserAdi",text="Eser Adı",anchor=CENTER)
eserTablosu.heading("eserBasim",text="Eser Basım",anchor=CENTER)
eserTablosu.heading("eserURL",text="Eser URL",anchor=CENTER)

for index, eser in enumerate(sonuc.fetchall()):
    eserTablosu.insert(parent='',index='end',iid=index,text='',
    values=(eser[0],eser[1],eser[2],eser[3]))

eserTablosu.pack()
pencere.mainloop()