from tkinter import * 
pencere=Tk()
pencere.geometry("600x400+100+100")
#pencere.title("Menu Programi",font="Times 20")
menu=Menu(pencere,font="Times 20")
pencere.config(menu=menu)
veri=Menu(menu,tearoff=0,font="Times 20")
menu.add_cascade(label="veri",menu=veri,font="Times 20") #ana başlık
veri.add_command(label="Veri Girme")
veri.add_command(label="Veri Sorma")
veri.add_command(label="Veri Listele")
veri.add_command(label="Çıkış",command=pencere.destroy)
incele=Menu(veri,tearoff=0,font="Times 20")
veri.add_cascade(label="incele",menu=incele)
incele.add_command(label="Bul")
incele.add_command(label="Degistir")
veri2=Menu(menu,tearoff=0)
menu.add_cascade(label="Analiz",menu=veri2)
veri2.add_command(label="Geniş Analiz",font="Times 20")
veri2.add_command(label="Standart Analiz",font="Times 20")

mainloop()