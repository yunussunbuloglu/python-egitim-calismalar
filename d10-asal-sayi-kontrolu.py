# Girilen bir sayının asal sayı olup olmadığını bulun

sayi = int(input('Sayı Giriniz: '))
aslami = True

if sayi == 1:
    aslami = False

for i in range(2,sayi):
    if sayi % i == 0:
        aslami = False
        break
if aslami:
    print('Sayı Asaldır!')
else:
    print('Sayı Asal Değil!')