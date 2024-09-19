""" Bankamatik Uygulaması """

"""
Dictionary lar fonksiyonların içerinde güncellendiğinde dışarda da güncellenir.

"""

yunusHesap = {
    'ad': 'Yunus Sunbuloglu',
    'hesapNo': '1234567',
    'bakiye': 3000,
    'ekhesap': 2000

}
rabisHesap = {
    'ad': 'Rabia Sunbuloglu',
    'hesapNo': '7654321',
    'bakiye': 2000,
    'ekhesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz')
        bakiyeSorgulama(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekhesap']

        if toplam >= miktar:
            ekHesapKullanımı = input('ek hesap kullanılsın mı(E/H): ')

            if ekHesapKullanımı == 'e':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekhesap'] -= ekhesapKullanilacakMiktar
                print('paranızı alabilirsiniz')
                bakiyeSorgulama(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bakiyeniz bulunmaktadır.")
        else:
            print('Yetersiz Bakiye')
            bakiyeSorgulama(hesap)

def bakiyeSorgulama(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekhesap']}TL dir.")


paraCek(yunusHesap,3000)


print('*'*50)
paraCek(yunusHesap,2000)
