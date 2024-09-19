""""""
# *************** Sayfanın Herhangi Bir Yerinde Güncelleme Yapma (Mevcut verileri değiştirir)
"""
    ** r+ modu ile dosya üzerinde hem okuma hem yazma yapabiliyoruz.
"""

"""
with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())

with open("newfile.txt","r+",encoding="utf-8") as file:
    file.seek(20)
    file.write("Rabia")
"""
"""
    ** İmleç dosyanın en başında olduğu için dosyanın başında parantez içerisindeki değeri yazar
       sonra dosyanın kalan değerlerini yazar.
    ** Bu işlemi 'w' modunda yazarsak dosyayı temizler ve sadece parantez içerisindeki değeri alırız.
    ** Eğer güncelleme işlemini yapmadan önce seek metodu ile imleci istediğimiz konuma getirirsek 
       getirdiğimiz konumda istediğimiz güncellemeyi yapar.
    ** Bu güncellemeler esnasında güncelleme yapacağı yerdeki veriyi silerek oraya yazar. 
"""
# *************** Sayfa Sonunda Güncelleme Yapma
"""
with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("\nSumSum Rabişi Seviyor")

with open("newfile.txt", "r", encoding="utf-8") as file:
        print(file.read())

"""
"""
    ** a modu ile dosya üzerinde yapacağımız tüm değişiklikler dosyanın sonuna eklenir.
    ** Sonda ekleme yaptığımız için cümleye \n ile başladık ki yeni verileri alt satırda göstersin
"""

# *************** Sayfa Başında Güncelleme Yapma
"""
with open("newfile.txt","r+",encoding="utf-8") as file:
    x = file.read()
    x = "Rabiş SumSumu Seviyor\n" + x       # bu şekilde çıktıda bilgiyi görürüz ama dosyaya işlemez.
    file.seek(0)                            # önce cursor 0. byte getirilir.
    file.write(x)                           # sonra write ile yukarda oluşturduğumuz update dosyaya tekrar yazdırılır.

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
"""

# *************** Sayfa Ortasında Güncelleme Yapma

with open("newfile.txt", "r+", encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(1,"aşk pıtırcıkları\n") # 1. indexten önce verdiğimiz objeyi ekledi. Ama dosyaya eklemedi.
    file.seek(0)
    file.writelines(liste)

#    for i in liste:                                     # alternatifi writeline
#        file.write(i)
with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())