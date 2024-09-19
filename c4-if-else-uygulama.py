
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

sayi = float(input('Sayı: '))

if sayi > 0 and sayi < 100:
    print("Sayı 0 ile 100 arasındadır")
else:
    print("Sayı 0-100 arasında değildir.")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz

sayi = float(input('Sayı: '))

if sayi > 0:
    if sayi % 2 == 0:
        print("Sayı pozitif Çift Sayıdır.")
    else:
        print("Sayı pozitif tek sayıdır.")
else:
    if sayi % 2 == 0:
        print("Sayı negatif Çift Sayıdır.")
    else:
        print("Sayı negatif tek sayıdır.")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız

girilen_email = input('Email: ')
girilen_password = input('parola: ')

email = 'ys@gmail.com'
password = 'abc123'

if girilen_email == email:
    if girilen_password == password:
        print("Giriş Başarılı.")
    else:
        print("Email doğru Şifre hatalı")
else:
    if girilen_password == password:
        print("Email hatalı Şifre Doğru")
    else:
        print("Email ve Şifre hatalı")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız

x1 = int(input('1.Sayı: '))
x2 = int(input('2.Sayı: '))
x3 = int(input('3.Sayı: '))

if x1 > x2:
    if x1 > x3:
        if x2 > x3:
            print("x1 > x2 > x3")
        else:
            print("x1 > x3 > x2")
    else:
        print("x3 > x1 > x2")
elif x2 > x3:
    if x1 > x3:
        print("x2 > x1 > x3")
    else:
        print("x2 > x3 > x1")
else:
    print("x3 > x2 > x1")

# 5- kullanıcıdan 2 vize ve final notunu alıp ortalamayı hesaplayın
#    Eğer ortalama 50 den yüksekse geçti değilse kaldı yazdırın
#    a-) Ortalama 50 den büyük olsa bile finalden 50 alma şartı olsun
#    b-) Finalden 70 alırsa ortalamaya bakılmasın

v1 = float(input('1.Vize: '))
v2 = float(input('2.Vize: '))
final = float(input('Final: '))
ort = v1*0.3 + v2*0.3 + final*0.4

if final <= 70:
    if ort >= 50:
        if final >= 50:
            print(f"ortalamanız : {ort} ve final notunuz: {final} olduğu için dersten geçtiniz.")
        else:
            print(f"ortalamanız : {ort} ve final notunuz: {final} final notunuz düşük olduğu için dersten kaldınız.")
    else:
        print(f"ortalamanız: {ort} ve final notunuz: {final} olduğu için dersten kaldınız.")
else:
    print(f"final notunuz: {final} olduğu için dersten geçtiniz.")

# 6- kişinin ad, kilo ve boy bilgilerini alıp kilo indeksini hesaplayın
#    Formül = (kilo / boyun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4 => zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => fazla kilolu
#    30.0-34.9 => şişman

ad = (input('Adınız:  '))
kg = float(input('Kilonuz: '))
hg = float(input('boyunuz (m): '))

boy_indexi = round((kg) / (hg ** 2),2)


if boy_indexi < 18.4:
    print(f"{ad} kilon: {kg} ve boyun: {hg} boy indeksin ise: {boy_indexi} derece - zayıf")
elif 18.4 < boy_indexi <= 24.9:
    print(f"{ad} kilon: {kg} ve boyun: {hg} boy indeksin ise: {boy_indexi} derece - normal")
elif 24.9 < boy_indexi <= 29.9:
    print(f"{ad} kilon: {kg} ve boyun: {hg} boy indeksin ise: {boy_indexi} derece - fazla kilolu")
elif 29.9 < boy_indexi <= 34.9:
    print(f"{ad} kilon: {kg} ve boyun: {hg} boy indeksin ise: {boy_indexi} derece - obez")
else:
    print("İndex bilgileriniz değerlerin dışında kalmıştır.")