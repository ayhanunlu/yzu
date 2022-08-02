from tkinter import *
import tkinter.messagebox
pencere=Tk()
pencere.geometry("700x400+200+200")
global kut
global say
say=-1

try:
    with open("veri.dat","r",encoding="utf-8") as dosya:
        kut=dosya.readlines()
except FileNotFoundError:
    kut=[]

def vericek():
    try:
        with open("veri.dat","r",encoding="utf-8") as dosya:
            kut=dosya.readlines()
    except FileNotFoundError:
        kut=[]
    return kut
def veriyaz(kut):
    with open("veri.dat","w",encoding="utf-8") as dosya:
        dosya.writelines(kut)


    




def verisorma():
    global kut
    global say
    

    
    kut=vericek()
    def vsorma():
        global say
        aranan=arasor.get()
        toplamveri=len(kut)
        if say<-1 or say>toplamveri:
            say=-1
        while say<toplamveri-1:
            say+=1
            print (say)
            if say>toplamveri:
                say=0
            
            ara=kut[say].split(",") # tek tek listedeki elemanları virgüllerden ayır
            ara[2]=ara[2].strip("/n")
            kontrolet=aranan in ara[0]
            if kontrolet==True:
                adgir.delete(0,"end")
                adgir.insert(0,ara[0])
                telgir.delete(0,"end")
                telgir.insert(0,ara[1])
                emailgir.delete(0,"end")
                emailgir.insert(0,ara[2])
                sil["state"]=NORMAL
                duzelt["state"]=NORMAL
                break
    def sil():
        global say
        global kut
        kut=vericek()
        cevap=tkinter.messagebox.askquestion(title="Dikkat Silinecek", message="Eminmisiniz?")
        #print (type(cevap))
        if cevap=="yes":
            kut.pop(say)
            veriyaz(kut)
            tkinter.messagebox.showinfo("Tamamlandı","Veri Silindi")
            sil["state"]=DISABLED
            duzelt["state"]=DISABLED

            pass

        else:
            pass
    def duzelt():
        global say
        global kut
        kut=vericek()
        kut2=adgir.get()+","+telgir.get()+","+emailgir.get()+"\n"
        kut.insert(say,kut2)
        kut.pop(say+1)
        veriyaz(kut)
        tkinter.messagebox.showinfo("Tamamlandı","Veri Düzeltildi...")
        duzelt["state"]=DISABLED
        sil["state"]=DISABLED







                

                
            

            
  
     
                


    frame2=Frame(pencere)
    araetiket=Label(frame2,font="Times 20",text="Aranan Kişi:")
    arasor=Entry(frame2,font="Times 20")
    ara=Button(frame2,font="Times 20",text="Ara",command=vsorma)
    cikk=Button(frame2,font="Times 20",text="İptal",command=frame2.destroy)
    ad=Label(frame2,font="Times 20",text="Adı-Soyad:")
    adgir=Entry(frame2,font="Times 20")
    tel=Label(frame2,font="Times 20",text="Tel:")
    telgir=Entry(frame2,font="Times 20")
    email=Label(frame2,font="Times 20",text="E-mail:")
    emailgir=Entry(frame2,font="Times 20")
    duzelt=Button(frame2,font="Times 20",text="Düzelt",command=duzelt)
    sil=Button(frame2,font="Times 20",text="sil",command=sil)



    araetiket.grid(row=1,column=1)
    arasor.grid(row=1,column=2,pady=30)
    ara.grid(row=1,column=3)
    cikk.grid(row=1,column=4)
    ad.grid(row=3,column=1)
    adgir.grid(row=3,column=2,pady=10)
    tel.grid(row=4,column=1)
    telgir.grid(row=4,column=2,pady=10)
    email.grid(row=5,column=1)
    emailgir.grid(row=5,column=2,pady=10)
    duzelt.grid(row=3,column=3)
    sil.grid(row=3,column=4)


    frame2.grid()
    sil["state"]=DISABLED
    duzelt["state"]=DISABLED

    frame2.mainloop()
    


         

        
def veriekle():
    global kut
    def verikaydet():
        try:
            with open("veri.dat","r",encoding="utf-8") as dosya:
                kut=dosya.readlines()

        except FileNotFoundError:
            kut=[]
        print (kut)
        kut2=adgir.get()+","+telgir.get()+","+emailgir.get()+"\n"
        kut.append(kut2)
        with open("veri.dat","w",encoding="utf-8") as dosya:
            dosya.writelines(kut)
        tkinter.messagebox.showinfo("Dikkat","Veri Kaydedildi...")
        frame1.destroy
        


   
    

    frame1=Frame(pencere)
    ad=Label(frame1,font="Times 20",text="Adı-Soyad:")
    adgir=Entry(frame1,font="Times 20")
    tel=Label(frame1,font="Times 20",text="Tel:")
    telgir=Entry(frame1,font="Times 20")
    email=Label(frame1,font="Times 20",text="E-mail:")
    emailgir=Entry(frame1,font="Times 20")
    kaydet=Button(frame1,font="Times 20",text="Kaydet",command=verikaydet)
    cik=Button(frame1,font="Times 20",text="İptal",command=frame1.destroy)



    ad.grid(row=1,column=1)
    adgir.grid(row=1,column=2,pady=10)
    tel.grid(row=2,column=1)
    telgir.grid(row=2,column=2,pady=10)
    email.grid(row=3,column=1)
    emailgir.grid(row=3,column=2,pady=10)
    kaydet.grid(row=1,column=3)
    cik.grid(row=2,column=3)


    
    frame1.grid()
    frame1.mainloop()


menu=Menu(pencere)
pencere.config(menu=menu)
dosya=Menu(menu,tearoff=0)
menu.add_cascade(label="Dosya",menu=dosya)
dosya.add_command(label="Veri Girme",command=veriekle)
dosya.add_command(label="Veri Sorma",command=verisorma)
dosya.add_command(label="Veri Listele")
dosya.add_command(label="Çıkış",command=pencere.destroy)


pencere.mainloop()