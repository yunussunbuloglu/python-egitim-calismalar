"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı iafadeleri ile buldurmaya çalışın (Hak = 5)
    ** "random modülü" için python random şeklinde bir arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""
import random

sayi = random.randint(1,10)            # 1 ile 100 arasında rastgele tam sayı üretir.
can = int(input('Kaç Hak Kullanmak İstersiniz: '))  # Soru başına puan hesaplarken kullanmak için ayrıca sabit olarak sakladık.
hak = can
sayac = 0


while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler Bilginiz. {sayac}. defada bildiniz. Toplam puanınız: {100 - ((100/can)* ((sayac)-1))}')
        break
    elif sayi > tahmin:
        print('Yukarı!')
    else:
        print('Aşağı!')
    if hak == 0:
        print(f'Hakkınız Bitti! Tutulan Sayı: {sayi}')
