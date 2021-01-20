from tkinter import *
import tkinter.messagebox
pencere=Tk()
pencere.title("Rehber Programı 1.0")
pencere.geometry("600x300+100+100")
global aramaindex
global toplamkayit
aramaindex=-1
def verikontrol(kut):
    try:
        with open("verireh.dat","r",encoding="utf-8") as dosya:
            kut=dosya.readlines()
            return kut
    except FileNotFoundError:
        kut=[]
        print ("Hata Var")
kut=[]
kut=verikontrol(kut)

        
def veriyaz(kut):
    with open("verireh.dat","w",encoding="utf-8") as dosya:
        dosya.writelines(kut)
def veriekle(ad,tel,email,kut):
    kut.append(ad+","+tel+","+email+"\n")
    veriyaz(kut)
    tkinter.messagebox.showinfo("Veri Ekleme", "Veri Kaydedildi")
    
    return kut
def verigir():
    
    def verikaydet():
        #print (kut)
        verikontrol(kut)
        veriekle(adtext.get(),teltext.get(),emailtext.get(),kut)
        

    frame1=Frame(pencere)
    
    adetiket=Label(frame1,text="Ad-Soyad:",font="Times 20")
    adtext=Entry(frame1,font="Times 20")
    teletiket=Label(frame1,text="Tel:",font="Times 20")
    teltext=Entry(frame1,font="Times 20")
    emailetiket=Label(frame1,text="E-mail:",font="Times 20")
    emailtext=Entry(frame1,font="Times 20")
    cik=Button(frame1,text="Cik",font="Times 20",command=frame1.destroy)
    kaydet=Button(frame1,text="Kaydet",font="Times 20",command=verikaydet)

    frame1.grid()
    
    adetiket.grid(row=1,column=1,padx=0,pady=10)
    adtext.grid(row=1,column=2,padx=10)
    teletiket.grid(row=2,column=1,padx=0,pady=10)
    teltext.grid(row=2,column=2,padx=10)
    emailetiket.grid(row=3,column=1,padx=0,pady=10)
    emailtext.grid(row=3,column=2,padx=10)


    kaydet.grid(row=1,column=3,pady=10)
    cik.grid(row=2,column=3)
    frame1.mainloop()
    
def verilistele():
    frame3=Frame(pencere)
    liste=Listbox(frame3,font="Times 15")
    tus=Button(frame3,font="Times 20",text="Çık",command=frame3.destroy)
    verikontrol(kut)
    print (kut)
    for i in kut:
        liste.insert(END, i)


    frame3.grid()
    liste.grid(row=1,column=1,padx=10,pady=10)
    tus.grid(row=1,column=2)

    frame3.mainloop()
def verisor():
    verikontrol(kut)
    toplamkayit=len(kut)
    
    def duzelt():
        global aramaindex
        #pop(aramaindex)
        ad=ad2text.get()
        tel=tel2text.get()
        email=email2text.get()
        kut2=ad+","+tel+","+email
        kut.pop(aramaindex)
        kut.insert(aramaindex,kut2)
        veriyaz(kut)
        tkinter.messagebox.showinfo("Düzeltme", "Düzeltme Tamamlandı")


    def aramayap():
        global aramaindex
        
        
        while aramaindex<=toplamkayit-1:
            
            aramaindex+=1
            if aramaindex>=toplamkayit:
                aramaindex=0
            kut2=kut[aramaindex]
            kut3=kut2.split(",")
            #print (kut3[1]) #aranan yer
            r=aranantext.get()
            kont=r in kut3[0]
            if kont==True:
                ad2text.delete(0,"end") #kutunu içini sil
                ad2text.insert(0,kut3[0])
                tel2text.delete(0,"end")
                tel2text.insert(0,kut3[1])
                email2text.delete(0,"end")
                email2text.insert(0,kut3[2])            
                #kaydet2(state=NORMAL)
                kaydet2["state"]="normal"
                break

        
    frame2=Frame(pencere)
    arananetiket=Label(frame2,text="Aranan Kişi:",font="Times 20")
    aranantext=Entry(frame2,font="Times 20")
    ad2etiket=Label(frame2,text="Ad-Soyad:",font="Times 20")
    ad2text=Entry(frame2,font="Times 20")
    tel2etiket=Label(frame2,text="Tel:",font="Times 20")
    tel2text=Entry(frame2,font="Times 20")
    email2etiket=Label(frame2,text="E-mail:",font="Times 20")
    email2text=Entry(frame2,font="Times 20")
    cik2=Button(frame2,text="Cik",font="Times 20",command=frame2.destroy)
    kaydet2=Button(frame2,text="Düzelt",font="Times 20",state=DISABLED,command=duzelt)
    sil=Button(frame2,text="Sil",font="Times 20",state=DISABLED)
    
    

    arama=Button(frame2,text="Ara",font="Times 20",command=aramayap)


    frame2.grid()
    arananetiket.grid(row=1,column=1,pady=10)
    aranantext.grid(row=1,column=2,pady=10)
    ad2etiket.grid(row=4,column=1,padx=0,pady=20)
    ad2text.grid(row=4,column=2,padx=10)
    tel2etiket.grid(row=5,column=1,padx=0,pady=10)
    tel2text.grid(row=5,column=2,padx=10)
    email2etiket.grid(row=6,column=1,padx=0,pady=10)
    email2text.grid(row=6,column=2,padx=10)

    arama.grid(row=1,column=3)
    kaydet2.grid(row=4,column=3,pady=10)
    cik2.grid(row=6,column=3)
    sil.grid(row=5,column=3)
    frame2.mainloop()


menu = Menu(pencere)
pencere.config(menu=menu)
dosya = Menu(menu,tearoff=0)
menu.add_cascade(label="Veri",menu=dosya) #ana başlık
dosya.add_command(label="Veri Girme",command=verigir)
dosya.add_command(label="Veri Sorma",command=verisor)
dosya.add_command(label="Veri Listele",command=verilistele)
dosya.add_command(label="Çıkış",command=pencere.destroy)


pencere.mainloop()