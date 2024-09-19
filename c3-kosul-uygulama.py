from datetime import datetime



# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#    Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise ya da üniversite olmalıdır


ad = input('adınız: ')
yas = int(input('yaşınız: '))
okul = input('Eğitim bilginiz: ')

if yas >= 18:
    if okul == 'lise':
        print('Alabilir')
    elif okul == 'üniversite':
        print('Alabilir')
    else:
        print('Eğitim durumu yetersiz')
else:
    print('Yaş değeriniz yetersiz.')



# 2- Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre puan aralığına gelen not bilgisini verelim.

# 0-24     -> 0
# 25-44    -> 1
# 45-54    -> 2
# 55-69    -> 3
# 70-84    -> 4
# 85-100   -> 5


y1 = int(input('1.yazılı notunuz: '))
y2 = int(input('2.yazılı notunuz: '))
s1 = int(input('sözlü notunuz: '))

ort = (y1 + y2 + s1)/3

if 0 <= ort <= 24:
    print(f'Puanınız: {ort:1.4} ve puanınıza karşılık gelen notunuz: 0')
elif 25 <= ort <= 44:
    print(f'Puanınız: {ort:1.4} ve puanınıza karşılık gelen notunuz: 1')
elif 45 <= ort <= 54:
    print(f'Puanınız: {ort:1.4} ve puanınıza karşılık gelen notunuz: 2')
elif 55 <= ort <= 69:
    print(f'Puanınız: {ort:1.4} ve puanınıza karşılık gelen notunuz: 3')
elif 70 <= ort <= 84:
    print(f'Puanınız: {ort:1.4} ve puanınıza karşılık gelen notunuz: 4')
else:
    print(f'Puanınız: {ort:1.4} ve puanınıza karşılık gelen notunuz: 5')

import datetime

# 3- trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.

# 1.bakım -> 1. yıl
# 2.bakım -> 2. yıl
# 3.bakım -> 3. yıl

tarih = input('Aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')
trafige_cıkıs = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafige_cıkıs

days = fark.days

if days <= 365:
    print('1.servis aralığı')
elif days>365 and days <= 365*2:
    print('2.servis aralığı')
elif days>365*2 and days <= 365*3:
    print('3.servis aralığı')
else:
    print('Hatalı değer')