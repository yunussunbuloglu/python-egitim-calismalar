"""
    def yazdıktan sonra fonksiyona bir isim verilir ve parantez açıp kapatılır. 
    parantez içerisine dışarıdan almak istediğimiz parametreler yazılır.

"""



def sayHello(name):
    print('hello '+ name)

sayHello('Yunus') # Hello Yunus yazar
sayHello('Rabia') # Hello Rabia yazar
#sayHello()        # Hata verir çünkü name değişkeni tanımlamadık.

def sayHello(name1 = "User"): # name değişkenine bir varsayılan değer atayarak fonksiyonu çağırırken değer göndermezsek hata vermek yerine bu değeri yazmasını sağlayabiliriz.
    print('hello '+ name1)

sayHello('Yunus') # Hello Yunus yazar
sayHello('Rabia') # Hello Rabia yazar
sayHello()        # Hello user yazar

def sayHello(name2 = "User"): # name değişkenine bir varsayılan değer atayarak fonksiyonu çağırırken değer göndermezsek hata vermek yerine bu değeri yazmasını sağlayabiliriz.
    return "Hello "+ name2

msg = sayHello('Yunus') # Hello Yunus yazar
print(msg)
msg = sayHello('Rabia') # Hello Rabia yazar
print(msg)
msg = sayHello()        # Hello user yazar
print(msg)

def total(num1, num2):
    return num1 + num2
toplam = total(10,20)
print(toplam)
toplam = total(15,20)
print(toplam)
toplam = total(10,45)
print(toplam)

def yasHesapla(dogumYili):
    return 2024 - dogumYili

yasYunus = yasHesapla(1995)
print(yasYunus)
yasRabia = yasHesapla(1993)
print(yasRabia)
print(yasYunus, yasRabia)

def emekliligeKacYilKaldı(dogumYili, isim):
    # Help komutu ile yazılımcılara fonksiyonun çalışma sistemi hakkında bilgi vermek için not bıraktık.
    """
    DOCSTRING: Dogum yilinize gore emekliliginize kac yil kaldi
    INPUT: Doğum Yili
    OUTPUT:Hesaplanan yil bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print('Zaten emekli oldunuz')

emekliligeKacYilKaldı(1995,"Yunus")
emekliligeKacYilKaldı(1993,"Rabia")