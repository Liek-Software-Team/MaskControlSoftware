import os
from tkinter import ttk
from tkinter import *
import tkinter as tk


window = Tk() #Pencere açıldı
window.geometry('450x250') #Pencerenin boyutları ayarlandı
def test():
    window.destroy() #Cascade kodlarının çalışması için pencereyi kapattık
    os.system('cmd /k "python .\\cascade.py"') #cascade kodları çalışıyor

def close(): #sistemi forced kapatmak için koyduk normal şekilde de çarpıdan kapanır bu da normal kapatır
    os.system('cmd /k "taskkill /F /IM "python.exe" /T"')

def open():#seçilen kameraya göre kamerayı açacak
    if camera_chosen.current() == 0:
        window.destroy()
        os.system('cmd /k "python .\\camera1.py"') #1 nolu default kamerayı açan kod
    elif camera_chosen.current() == 1:
        window.destroy()
        os.system('cmd /k "pyton .\\camera2.py"') # ekstra kamera varsa onu açar

def test1(): #kamera var mı diye test ediyor python shellde yazınca gözükür 0 döndürüyorsa kamera 1 hazır demektir.
    print(camera_chosen.current())

window.title("Mask Control Software") #Uygulama penceresinin adı
#Genel label açıldı text kısmında ismi background resmin arka planını belirliyor içerideki yazıların rengi foreground ile belirli
#font kısmında yazı tipi ve puntosu mevcut. grid fonksiyonları konumunu belirler ortalamak için column 1 seçildi
ttk.Label(window, text = "Mask Control Software",background = 'skyblue2', foreground ="white",font = ("Times New Roman", 19)).grid(row = 0, column = 1)

#Seçilebilecek kameraları belirtmek için ekledik text kısmında seçilecek kamera için ibare yer almaktadır.
#font kısmında punto ve yazı tipi yine gridde de konumu var ve yazının etrafında 10 birime 25 birimlik boşluk var böylece combobox ile çakışmıyorlar
ttk.Label(window, text = "Choose Camera :",font = ("Times New Roman", 10)).grid(column = 0, row = 5, padx = 10, pady = 25)

# combobox için string açıldı
n = tk.StringVar()
#combobox için ttk'dan eleman çağırıldı
camera_chosen = ttk.Combobox(window, width = 27, textvariable = n)

# camera1 ve camera2 seçenekleri eklendi artırmak isterseniz camera3,4 gider
# Yeni kamera ekledikten sonra yukarıdaki open fonksiyonunda if bloğuna da eklemeniz lazım aynı mantıkta 1 artırarak ilerleyin
# camera.py dosyalarından bir tane daha açarak örn camera3.py diye açın içine girin
camera_chosen['values'] = ('Camera 1', 'Camera 2')
#comboboxın yeri grid fonksiyonu ile belirtildi. 5.satırda ve ortalanmış vaziyette yer alıyor
camera_chosen.grid(column = 1, row = 5)
camera_chosen.current()
#3 adet buton eklemesi yapılıyor bgler arka font rengi, fgler de yazı rengi
#Command parametresi fonksiyon blokları içerir. İçerisine kendi yazdığınız bir fonksiyon ekleyebilirsiniz.
btn = Button(window, text="Start Camera",bg='skyblue2',fg='white', command=open,height=2, width=10)
btn2 = Button(window, text="Close", bg='red',fg='white',command=close)
btn3 = Button(window, text = "Test", bg='blue',fg='white',command=test)
btn.grid(column=1, row=6, padx=3,pady=3)
btn2.grid(column =1,row = 10)
btn3.grid(column=1,row=7)

#Versiyon numarası belirtmek için en alt kısma da bu label eklendi
ttk.Label(window, text = "Version 1.0.0",font = ("Times New Roman", 10)).grid(column = 12, row = 10, padx = 10, pady = 25)
window.mainloop() #GUI'nin while1 şeklinde çalışmasını sağlar
