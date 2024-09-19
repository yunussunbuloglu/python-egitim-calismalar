# 1- " BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturun.

x = ['BMW', 'Mercedes', 'Opel', 'Mazda']
print(x)

# 2- Liste kaç elemanlıdır?

x1 = len(x)
print(x1)

# 3- Listenin ilk ve son elemanı nedir?

x2 = x[0]
x3 = x[len(x)-1]
print(x2)
print(x3)

# 4- Mazda değerini toyota ile değiştirin.

x[3] = 'Toyota'
x4 = x 
print(x4)

# 5- Mercedes listenin kaçıncı elemanıdır?

x5 = x.index('Mercedes')
x5 = 'Mercedes' in x
print(x5)

# 6- Listenin -2. indexindeki eleman nedir?

x6 = x[-2]
print(x6)

# 7- Listenin ilk 3 elemanını alın

x7 = x[:3]
print(x7)

# 8- Listenin son iki elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin

x[-2:] = ['Toyota', 'Reanult']
x8 = x
print(x8)

# 9- listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin

x9 = ['Audi', 'Nissan']
x9 = x + x9
print(x9)

# 10- Listenin son elemanını silin

"""
x.pop()
x10 = x 
print(x10)
şeklinde yaparsakta listenin son elemanını siler. parantezler içerisine bir index girilirse o indexteki elemanı siler.
"""
del x[-1]
x10 = x
print(x10)

# 11- Liste elemanlarını tersten yazdırın

x11 = x[::-1]
print(x11)

# 12- Aşağıdaki verileri bir liste içinde saklayınız

    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan 1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)

notA = [70, 60, 70]
notB = [80, 80, 70]
notC = [80, 70, 90]

stA = ['Yiğit', 'Bilgi', 2010, notA]    # stA = ['Yiğit', 'Bilgi', 2010, [70, 60, 70]]
stB = ['Sena', ' Turan', 1999, notB]    # stB = ['Sena', ' Turan', 1999, [80, 80, 70]]
stC = ['Ahmet', ' Turan', 1998, notC]   # stC = ['Ahmet', ' Turan', 1998, [80, 70, 90]]

st = [stA, stB, stC]

# 13- liste elemanlarını ekrana yazdırın

print(st)

yb = f"{stA[0]} {stA[1]} {2024 - stA[2]} yaşında ve not ortalaması {((stA[3][0] + stA[3][1] + stA[3][2])/3):1.5}" 
# Sondaki :1.5 ifadesi ortalamada toplamda 5 sayı göreceğimiz anlamına gelir.

print(yb)