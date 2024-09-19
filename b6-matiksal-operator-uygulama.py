# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol edin.

a = float(input('Bir Sayı Giriniz: '))
a1 = (0 < a) and (a <= 100)
print(f'0 < {a} <= 100 sağlıyor mu: {a1}')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol edin.

a2 = float(input('Bir Sayı Giriniz: '))
a3 = (a > 0) and (a % 2 == 0)
print(f'girilen değer pozitif çitf sayı mıdır? {a3}')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız

girilen_email = input('Email: ')
girilen_password = input('parola: ')

email = 'ys@gmail.com'
password = 'abc123'

a4 = (email == girilen_email) and (password == girilen_password)

print(f'Sisteme giriş onay durumu: {a4}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız

x1 = int(input('1.Sayı: '))
x2 = int(input('2.Sayı: '))
x3 = int(input('3.Sayı: '))

a5 = x1 > x2 and x1 > x3
print(f'1. sayı en büyük: {a5}')
a5 = x2 > x1 and x2 > x3
print(f'2. sayı en büyük: {a5}')
a5 = x3 > x2 and x1 < x3
print(f'3. sayı en büyük: {a5}')

# 5- kullanıcıdan 2 vize ve final notunu alıp ortalamayı hesaplayın
#    Eğer ortalama 50 den yüksekse geçti değilse kaldı yazdırın
#    a-) Ortalama 50 den büyük olsa bile finalden 50 alma şartı olsun
#    b-) Finalden 70 alırsa ortalamaya bakılmasın

v1 = float(input('1.Vize: '))
v2 = float(input('2.Vize: '))
final = float(input('Final: '))
ort = v1*0.3 + v2*0.3 + final*0.4

a6 = ort >= 50 and final > 50
a7 = ort >= 50 or final > 70

print(f'ortalama {ort:1.5} ve geçme durumu: {a6}')
print(f'ortalama {ort:1.5} ve geçme durumu: {a7}')

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

boy_indexi = (kg) / (hg ** 2)

zayif = (boy_indexi >= 0) and (boy_indexi <= 18.4)
normal = (boy_indexi > 18.4) and (boy_indexi <= 24.9)
kilolu = (boy_indexi > 24.9) and (boy_indexi <= 29.9)
obez = (boy_indexi > 29.9) and (boy_indexi <= 34.9)

print(f'{ad} kilo indeksin: {boy_indexi} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{ad} kilo indeksin: {boy_indexi} ve kilo değerlendirmen normal: {normal}')
print(f'{ad} kilo indeksin: {boy_indexi} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{ad} kilo indeksin: {boy_indexi} ve kilo değerlendirmen obez: {obez}')

