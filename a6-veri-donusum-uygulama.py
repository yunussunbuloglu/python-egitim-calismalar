'''
    Daire Alanı     : nr2
    Daire Çerçevesi : 2nr

    *Yarı çapı veerilen bir dairenin alan ve çevresini hesaplayınız. (n = pi = 3.14)
'''

r = float(input('Dairenin Yarı Çapını Giriniz: '))
n = 3.14
alan = n * (r ** 2)
print("Dairenin Alanı: ", alan, " m2")

cevre = 2*n*r
print("Dairenin Çevresi: ", cevre, "cm")

