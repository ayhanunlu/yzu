from tkinter import *
import tkinter.messagebox
pencere = Tk()
pencere.title("Rehber Programı 2.0")
pencere.geometry("600x400+100+100")
global kut

try:
    with open("veri.dat","r",encoding="utf-8") as dosya:
        kut=dosya.readlines()
        print (kut)
except FileNotFoundError:
    kut=[]
    print (kut)

def veriekle():
    
    
    

    
    def kaydet():
        kut2=adtext.get()+","+teltext.get()+","+emailtext.get()+","+str(var1.get())+","+str(var2.get())+","+str(var3.get())+"\n"
        kut.append(kut2)
        #print (kut)
        with open("veri.dat","w",encoding="utf-8") as dosya:
            dosya.writelines(kut)
            tkinter.messagebox.showinfo("Veri Kaydedildi", "Girdiğiniz veri kaydedilmiştir")


        #print (kut)
        
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    frame1=Frame(pencere)
    ad=Label(frame1,text="Ad-Soyad:",font="Times 20")
    adtext=Entry(frame1,font="Times 20")
    tel=Label(frame1,text="Tel:",font="Times 20")
    teltext=Entry(frame1,font="Times 20")
    email=Label(frame1,text="E-mail:",font="Times 20")
    emailtext=Entry(frame1,font="Times 20")
    kaydet=Button(frame1,text="Kaydet",font="Times 20",command=kaydet)
    cik=Button(frame1,text="Çık",font="Times 20",command=frame1.destroy)
    check1 = Checkbutton(frame1, text="Python",variable=var1, onvalue=1, offvalue=0,font="Times 20")
    check2 = Checkbutton(frame1, text="Visual Basic",variable=var2, onvalue=1, offvalue=0,font="Times 20")
    radio1 = Radiobutton(frame1, text='Bayan', variable=var3, value=0,font="Times 20")
    radio2 = Radiobutton(frame1, text='Bay', variable=var3, value=1,font="Times 20")
    ad.grid(row=1,column=1,padx=10,pady=10)
    adtext.grid(row=1,column=2,padx=0)
    tel.grid(row=2,column=1,padx=10,pady=10)
    teltext.grid(row=2,column=2,padx=0)
    email.grid(row=3,column=1,padx=10,pady=10)
    emailtext.grid(row=3,column=2,padx=0)
    check1.grid(row=4,column=1)
    check2.grid(row=4,column=2)
    radio1.grid(row=5,column=1)
    radio2.grid(row=5,column=2)
    kaydet.grid(row=1,column=3)
    cik.grid(row=2,column=3)

    

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
