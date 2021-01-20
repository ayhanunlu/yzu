from tkinter import *
pencere = Tk()
pencere.title("Rehber Programı 2.0")
pencere.geometry("600x400+100+100")

def veriekle():
    frame1=Frame(pencere)
    ad=Label(frame1,text="Ad-Soyad:",font="Times 20")
    adtext=Entry(frame1,font="Times 20")

    ad.grid(row=1,column=1,padx=10,pady=10)
    adtext.grid(row=1,column=2,padx=0)
    
    frame1.grid()
    
    frame1.mainloop()


menu = Menu(pencere)
pencere.config(menu=menu)
dosya = Menu(menu,tearoff=0)
menu.add_cascade(label="Veri",menu=dosya) #ana başlık
dosya.add_command(label="Yeni Kayıt",font="Times 20",command=veriekle)
dosya.add_command(label="Veri Sorma",font="Times 20")
dosya.add_command(label="Listeleme",font="Times 20")
dosya.add_command(label="Çıkış",font="Times 20",command=pencere.destroy)
pencere.mainloop()
