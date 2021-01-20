from tkinter import *
pencere = Tk()
menu = Menu(pencere)
pencere.config(menu=menu)
dosya = Menu(menu,tearoff=0)
menu.add_cascade(label="Dosya",menu=dosya) #ana başlık
dosya.add_command(label="Aç")
dosya.add_command(label="Kaydet")
dosya.add_command(label="Farklı Kaydet...")
dosya.add_command(label="Çıkış",command=pencere.quit)
pencere.mainloop()
