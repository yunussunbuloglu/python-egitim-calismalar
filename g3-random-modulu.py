""""""

import random
"""
x = dir(random)
x = help(random)

"""

x = random.random()                       # 0.0 ile 1.0 arası rastgele bir sayı üretir.
x = random.random() * 100                 # üretilen sayıyı 100 ile çarpabiliriz
x = int(random.uniform(1,10))       # 1 ile 10 arasında sayı üretir. int ile tam kısmını alabiliriz.
x = random.randint(1,10)            # 1 ile 10 arasında tam sayı üretir.

names = ['yunus', 'rabia', 'emre', 'cennet']
str = "hello there"

x = names[random.randint(0,len(names)-1)]      # liste içerisinden rastgele bir eleman alır. len eleman sayısı ama index 1 eksik numarada biteceği için 1 çıkarttık.
x = random.choice(names)                          # yukardaki işlemi yapan fonksiyon
y = random.choice(str)

liste = list(range(10)) # sıralı liste oluşturur
z = liste
random.shuffle(liste)   # oluşturulan listenin elemanlarını random sıralar.
z = liste

liste2 = range(100)
x2 = random.sample(liste,3) # adı belirtilen listenin elemanlarından belirtilen sayıda elemanları rastgele seçer
x3 = random.sample(names, 2)

print(x)
print(y)
print(z)
print(x2)
print(x3)


