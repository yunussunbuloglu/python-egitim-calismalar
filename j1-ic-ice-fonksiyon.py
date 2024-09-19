""""""

def greeting(name):
    print("hello",name)

print(greeting("yunus"))
print(greeting)

sayHello = greeting     #Burada obje ataması değil objenin tutulduğu adres ataması yapılıyor. böylelikle sayHello da fonk gibi çalışır.


"""  ** Yukardaki işlem sayesinde sayHello değişkeni ile greeting fonksiyonu aynı adresi tanımlar hale geldi.
        Böylece greeting(yunus) ile sayHello(yunus) ynı çıktıyı verir hale geldi. 
     ** Eğer sayHello işlemi del ile silinirse greeting() fonksiyonu halla bellekte tutuluyor olur. 
"""

print(greeting("yunus"))
print(sayHello("yunus"))    # çıktısında ikiside aynı sonucu verecek

del sayHello                # bu işlemle objeyi değil tanımladığımız adresi silmiş olduk.

print(greeting)     # çıktısında greeting fonksiyonunun bellekte tutulduğu adresi verir.

def outer(num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)
    """  Dışardaki fonksiyon çağırıldığında içerdeki fonksiyon çalışmaz. Çalışması için fonksiyonu 
    dış fonksiyonun kod bloğu içerisinde çağırmamız gerekiyor. Return ettiği değeri görebilmek ve işleyebilmek için
    başka bir değişkene atamasını yaptık. Böylelikle dışarda dış fonksiyonu çağırdığımızda num1 yerine örnekteki gibi 
    10 bilgisi gelecek ve 1 ekleyerek num2 değerine atayacak. Bu şekilde iç içe fonksiyon kullanımına kapsülleme denir.
    
    """

outer(10)       # sadece dışardaki fonksiyon çağırıldığı için içerdeki fonksiyon çalışmadı.
                # Sonradan iç fonksiyonu dış fonksiyonun kod bloğu içerisinde çağırdığımız
                # için iç fonksiyonda çalışmaya başlayacak.
""" İç fonksiyonu dışarda çağırırsak çalışmaz. """

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if not number >= 0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1

        return number * inner_factorial(number - 1)

    return inner_factorial(number)
try:
    print(factorial(5))
except Exception as ex:
    print(ex)