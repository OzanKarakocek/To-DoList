import json
import os.path
import tkinter
from PIL import Image, ImageTk

DOSYA_ADI = "notlar.json"

def notlari_yukle():
    if os.path.exists(DOSYA_ADI):
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    return []

def notlari_kaydet():
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(notlar, dosya, ensure_ascii=False, indent=4)

def not_ekle():
    not_metni = not_giris.get()
    if not_metni:
        notlar.append(not_metni)
        liste.insert(tkinter.END, not_metni)
        not_giris.delete(0, tkinter.END)
        notlari_kaydet()

def not_sil():
    secili = liste.curselection()
    if secili:
        index = secili[0]
        liste.delete(index)
        del notlar[index]
        notlari_kaydet()

notlar = notlari_yukle()

screen = tkinter.Tk()
screen.title("To-Do List")
screen.config(width=500, height=500)
screen.resizable(width=False, height=False)

logo = Image.open("logo.jpeg")
resized_logo = logo.resize((100, 100))
logo = ImageTk.PhotoImage(resized_logo)

logo_label = tkinter.Label(screen, image=logo)
logo_label.pack(pady=20)

giris_label = tkinter.Label(text="Notunuzu Giriniz: ", bg="white", fg="black")
giris_label.pack(pady=10)

not_giris = tkinter.Entry(screen, width=40, font=("Arial", 14), fg="black")
not_giris.pack(pady=10, ipady=20)

kaydet_button = tkinter.Button(text="Notu Kaydet", bg="white", fg="black", command=not_ekle)
kaydet_button.pack(pady=20)

liste = tkinter.Listbox(screen, width=40, height=10)
liste.pack(pady=5)

sil_button = tkinter.Button(screen, text="Sil", command=not_sil)
sil_button.pack(pady=10)

for not_ in notlar:
    liste.insert(tkinter.END, not_)

screen.mainloop()
