def changeName(n):
    n = 'Rabia'
name = "Yunus"

changeName(name)
print(name)

def change(n):
    n[0]="istanbul"

sehirler = ["ankara", "izmir"]
change(sehirler)
print(sehirler)

x = ["ankara", "izmir"]
y = x[:]      # slicing yöntemi    # : koyarak x dizisinin bir kopyasını y dizisine attık o yüzden x üzerinden yaptığımız değişikler y yi etkilemedi. : koymazsak  
x[0] = "İstanbul"                  # x üzerinde yaptığımız tüm değişiklikler y yi de etkiler.

print(x)
print(y)

# slicing yönteminin fonksiyonlarda kullanımı

def change2(n2):
    n2[0] = "istanbul"

sehirler2 = ["ankara", "izmir"]

change2(sehirler2[:])

print(sehirler2)


def add(a, b, c=0, d=0, e=0):       # sadece a,b şeklinde tanımlarsak 3 değer geldiğinde hata verir o yüzden varsayılanı 0 olan değişkenler tanımladık.
    return sum((a,b))     # sum bir fonksiyon ve pythona gömülü olarak geliyor.

print(add(10,20))

def add(*params):        # 6 dan fazla değişken girilecekse *args yada *params şeklinde tanımlanmalı
    return sum((params))
print(add(10,20,50))
print(add(10,20,30))
print(add(10,20,30,50,60,10,20))

def add2(*params2):
    sum = 0

    for n in params2:
        sum = sum + n
    return sum

print(add2(10,20,50))
print(add2(10,20,30))
print(add2(10,20,30,50,60,10,20))

def displayUser(**params):                      # params yerine **args şeklinde de kullanılabilir.
                                                # ** ile dictinoary döner * ile tuple döner.
    for key,value in params.items():
        print(f"{key} is {value}")
displayUser(name = "Yunus", age = 29, city = "Gonya")
displayUser(name = "Rabiş", age = 31, city = "Garaman", phone = "123123")
displayUser(name = "Emre", age = 26, city = "Gayseri", phone = "123123123", email = "es@mail.com")

def myFunc(a, b, *args, **kwargs):
        print(a)
        print(b)
        print(args)
        print(kwargs)

myFunc(10, 20, 30,40, 50, key1 = "value1", key2 = "value2")



