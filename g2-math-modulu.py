""""""

import math as islem

# as ile kütüphaneye takma ad verilir ve bu ad ile ulaşılabilir

value = dir(math)                   # modülün içerisindeki fonksiyonların ismini verir
value = help(math)                  # modülün tüm fonsiyonlarını açıklamalı gösterir
value = help(math.factorial)        # modülün sadece seçilen fonsiyonlarını açıklamalı gösterir

x = math.sqrt(49)                   # Değerin karekökünü almaya yarayan fonksiyon ile 49 un karekökünü aldık
y = math.factorial(5)               # Değerin faktöriyelini almaya yarayan fonksiyon ile 5 in faktöriyelini aldık
z = math.floor(5.9)                 # Değerin aşağıya yuvarlanmasını sağlayan fonksiyon ile 5.9 u aşağı yuvarladık
z2 = math.ceil(5.9)                 # Değerin yukarıya yuvarlanmasını sağlayan fonksiyon ile 5.9 u yukarı yuvarladık

print(x)
print(y)
print(z)
print(z2)



# yöntem 2

from math import *
""" from math import factorial,sqrt,ceil şeklinde istediğimiz fonksiyonu import edebiliriz."""

# math modülündeki tüm fonksiyonları içeri aktarır.
# bu kullanıl ile math. şeklinde kullanmamıza gerek kalmaz.
# yıldız tüm fonksiyonları aktarır.
# yıldız yerine istediğimiz fonksiyonun adını yazarak sadece onu içeri aktarabiliriz.


a = sqrt(9)

print(a)