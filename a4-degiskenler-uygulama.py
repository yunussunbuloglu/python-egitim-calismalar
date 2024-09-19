"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz

    Müşteri Adı
    Müşteri Soyadı
    Müşteri Adı + Müşteri soyadı
    Müşteri cinsiyeti
    Müşteri TC kimlik no
    Müşteri Doğum yılı
    Müşteri adres bilgileri
    Müşteri Yaşı
"""

ad = 'Ali'
soyad = ' Arı'
musteri = ad+soyad
cinsiyet = 'Erkek'
tc_no = '11111111111'
musteri_dogum_yili = 1995
musteriAdres = 'Konya'
musteri_yasi = 2024 - musteri_dogum_yili


"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız

    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL

"""

siparis1 = 110 
siparis2 = 1100.5 
siparis3 = 356.95
tutar = siparis1 + siparis2 + siparis3
print('Tutar:', tutar)