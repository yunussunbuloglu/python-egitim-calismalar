"""
    ogrenciler{
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }
"""

# 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız

ogrenciler = {}

a = input('Öğrenci numarası: ')
b = input('Öğrencinin adını: ')
c = input('öğrencinin soyadı: ')
d = input('Öğrenciye ait telefon numarası: ')

ogrenciler.update({
    a: {
        'ad': b,
        'soyad': c,
        'telefon': d
    }
})

a = input('Öğrenci numarası: ')
b = input('Öğrencinin adını: ')
c = input('öğrencinin soyadı: ')
d = input('Öğrenciye ait telefon numarası: ')

ogrenciler.update({
    a: {
        'ad': b,
        'soyad': c,
        'telefon': d
    }
})

a = input('Öğrenci numarası: ')
b = input('Öğrencinin adını: ')
c = input('öğrencinin soyadı: ')
d = input('Öğrenciye ait telefon numarası: ')

ogrenciler.update({
    a: {
        'ad': b,
        'soyad': c,
        'telefon': d
    }
})


""" benim yöntem 
a1 = input('1.Öğrenci numarası: ')
b1 = input('1.Öğrencinin adını: ')
c1 = input('1.öğrencinin soyadı: ')
d1 = input('1.Öğrenciye ait telefon numarası: ')

a2 = input('2.Öğrenci numarası: ')
b2 = input('2.Öğrencinin adını: ')
c2 = input('2.öğrencinin soyadı: ')
d2 = input('2.Öğrenciye ait telefon numarası: ')

a3 = input('3.Öğrenci numarası: ')
b3 = input('3.Öğrencinin adını: ')
c3 = input('3.öğrencinin soyadı: ')
d3 = input('3.Öğrenciye ait telefon numarası: ')

ogrenciler = {
    a1 : {
        'ad': b1,
        'soyad': c1,
        'telefon': d1
    },
    a2 : {
        'ad': b2,
        'soyad': c2,
        'telefon': d2
    },
     a3 : {
         'ad': b3,
        'soyad': c3,
        'telefon': d3
    }
}

print(ogrenciler)

"""
print(ogrenciler)

# 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

x = input('Öğrenci No: ')

print(ogrenciler[x])
print(f"Aradığınız {x} nolu öğrencinin adı: {ogrenciler[x]['ad']} soyadı: {ogrenciler[x]['soyad']} ve telefon numarası: {ogrenciler[x]['telefon']} şeklindedir.")
