""""""
"""
    Normalde iç içe fonksiyon kullanırken içerdeki fonksiyonun çalışması için dış fonksiyon 
    bloğu içerisinde çağırılması gerekiyordu. Bunun yerine burada fonksiyondan geriye 
    fonksiyon döndürerek aynı işlemi yapmış oluyoruz.
    'two = usalma(2) işlemi ile dış fonksiyonu çalıştırıp number değişkenine 2 değerini atayarak
    geri dönüş olarak inner fonksiyonunu aldık. print(two(3)) ile inner fonksiyonunun değişkeni 
    olan power a 3 değerini atamış olduk. Böylelikle sonuç olarak 2 üssü 3 den 8 değerini aldık.
"""
def usalma(number):

    def inner(power):
        return number ** power
    return inner

two = usalma(2)      # bu değer yukarıda dış fonksiyondaki numberın yerine gelir
three = usalma(3)    # bu değer yukarıda dış fonksiyondaki numberın yerine gelir

print(two(3))        # bu değer yukarıda iç fonksiyondaki powerın yerine gelir
print(three(4))      # bu değer yukarıda iç fonksiyondaki powerın yerine gelir

def yetki_sorgula(page):
    def inner(role):
        if role == "Admin":
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
    return inner

user1 = yetki_sorgula("Product Edit")
print(user1("Admin"))       # Admin rolü Product Edit sayfasına ulaşabilir.
print(user1("User"))        # User rolü Product Edit sayfasına ulaşamaz.

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += 1
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print(toplama(1,3,4,5,6,7,8))

carpma = islem("carpma")
print(carpma(1,2,3,4,5,6))
