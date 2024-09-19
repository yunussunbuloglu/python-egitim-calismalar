""""""
""" 'r' metodu varsayılan olarak gelmekte. Eğer olmayan bir dosya adını girersek hata verir.
    Hatasını kontrol altına alarak programın durmasını engellemek için try-except bloğuna aldık.
"""
try:
    file = open("newfile.txt","r")
    print(file)

except FileNotFoundError:

    print("dosya okuma hatası")
finally:
    print("Dosya kapandı.")
    file.close()

file2 = open("newfile.txt","r",encoding="utf-8")

# *************** for döngüsü ile okuma yapma
"""
for i in file2:
    print(i, end="")     # print varsayılan olarak satırlar arasına bir boş satır ekliyor. end ile onu iptal ettik.
file2.close()
"""
# *************** read() fonksiyonu ile okuma yapma

x = file2.read()        # read ile okuma yaptığımızda print ilave bir boş satır eklemesi yapmaz.
print("içerik 1")
print(x)
print("içerik 2")
x2 = file2.read()
print(x2)
file2.close()

"""
    ** read ile okuma yaparken dosyanın tamamını okur ve imleç dosyanın sonunda olur. Bu yüzden 
    dosyayı kapatmadan yapacağımız ikinci ve daha fazla okumalarda boş dönecektir çünkü imleç
    ilk okumadan sonra dosyanın sonunda kaldı ve okuyacağı değer kalmadı.
    ** Bunun önüne geçmek için her okumadan sonra dosyanın kapatılması lazım.
    ** Yukarıdaki örnekte print(x2) boş dönecektir. Ancak x2 yi yazmadan önce file2.closed() yaparsak 
    ya da okuma işlemini (file2 = open("newfile.txt","r",encoding="utf-8")) x2 den önce yaparsak 
    dosyayı ikinci kez okutabiliriz.
"""

"""
file3 = open("newfile.txt","r",encoding="utf-8")

x3 = file3.read(5)
x4 = file3.read(5)

print(x3)
print(x4)
file3.close()
"""

""" ** Read fonksiyonunu çağırdıktan sonra parantez içerisine girilen değer kadar okuma yapar
    Eğer dosyayı kapatmadan tekrar çağırırsak; yukardaki örnekte olduğu gibi ilk print ile 5 karakteri okur
    buna 5 byte denir ve her karakter 1 byte olarak değerlendirilir.
    sonra ikinci print ile 6. karakterden itibaren 5 karakter daha okur. 
    NOT: Okuma işleminde boşluklarda bir karakter olarak değerlendirilmelidir. 
"""

# *************** readline() fonksiyonu ile okuma yapma

file4 = open("newfile.txt","r",encoding="utf-8")

x5 = file4.readline()   # readline her seferinde bir satır okur
print(x5,end="")
print(x5,end="")
print(x5,end="")
file4.close()

"""
    ** readline() ile bir satırı komple okuyabiliriz. Fakat bunda da for döngüsünde olduğu gibi print 1 satır boşluk bırakır.
    ** Dosyada 5 satır var ve 8 defa readline ile okuma yaparsak satırlar bittikten sonra 3 satırlık boşluk karakteri basar.
    Bunu önlemek için printin sonuna end="" ekledik. böylelikle 10 defa da yazdırsak dosyada kaç satır varsa o kadar yazar.
"""

# *************** readlines() fonksiyonu ile okuma yapma

file5 = open("newfile.txt","r",encoding="utf-8")

liste = file5.readlines()
print(liste)

print(liste[0])
print(liste[1])
print(liste[2])

file5.close()

"""
    ** readlines() fonksiyonu okuma yaptığı her bir satırı liste elemanına dönüştürür.
    ** Her eleman bir satır olduğu için sonunda '\n' gözükecektir.
    ** Listenin index numarasından her bir elemana ulaştığımızda sonunda '\n' gözükmez. 
"""