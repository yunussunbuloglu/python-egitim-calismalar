
# 1- Girilen 2 sayıdan hangisi küçüktür?
a = input('1.sayı: ')
b = input('2.sayı: ')

if a < b:
    print('1. Sayı 2. Sayıdan küçüktür.')
elif a > b:
    print('1. sayı 2.sayıdan büyüktür.')
else:
    print('iki sayı birbirine eşit.')

# 2- Kullanıcıdan 2 vize ve final notunu alıp ortalamasını hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

v1 = float(input('1. Vize Notu: '))
v2 = float(input('2. Vize Notu: '))
f = float(input('Final Notu: '))

x = (v1*0.30 + v2*0.30 + f*0.40)
if x >= 50:
    print('Geçtiniz.')
else:
    print('Kaldınız.')

# 3- Girilen bir sayının tek mi çift mi olduğunu kontrol edin.

a2 = int(input('Bir sayı giriniz: '))
x2 = a2 % 2

if x2 == 0:
    print('Çift Sayı girdiniz')
else:
    print('tek sayı girdiniz')

# 4- Girilen bir sayının negatiflik durumunu kontrol edin

x3 = int(input('Bir sayı giriniz: '))

if x3 < 0:
    print('negatif değer girdiniz')
elif x3 > 0:
    print('pozitif değer girdiniz')
else:
    print('sıfır girdiniz')

# 5- email ve parola bilgisi alıp doğruluğunu kontrol edin.
#    email: ys@gmail.com parola:abc123

x4 = input('mail adresini girin: ')
x5 = input('parolayı girin: ')

email = 'ys@gmail.com'
parola = 'abc123'

if email == x4 and parola == x5:
    print('parola ve mail doğru')
elif email == x4 and parola != x5:
    print('mail doğru parola yanlış')
elif email != x4 and parola == x5:
    print('mail yanlış parola doğru')
else:
    print('parola ve mail yanlış')