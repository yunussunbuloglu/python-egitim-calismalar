x = 5
y = 10
z = 20

x, y, z = 16, 10,20
print(x,y,z)

x, y = y, x  # x ve y değerleri birbirleri ile değiştirilmiş olur.
print(x,y,z)

x += 5 # x = x + 5 değeri ile aynı olup x in mevcut değerinin üstüne 5 ekler.
print(x,y,z)

x -= 5 # x = x - 5 değeri ile aynı olup x in mevcut değerinden 5 çıkartır.
print(x,y,z)

x *= 5 # x = x * 5 değeri ile aynı olup x in mevcut değerini 5 ile çarpar
print(x,y,z)

x /= 5 # x = x / 5 değeri ile aynı olup x in mevcut değerini 5 e böler
print(x,y,z)

x %= 5 # x = x % 5 değeri ile aynı olup x in 5 ile bölümünden kalanı x e değer olarak verir
print(x,y,z)

y //= 5 # y = y // 5 değeri ile aynı olup y in mevcut değerini 5 ile bölerek tam kısmını değer olarak atar.
print(x,y,z)

y **= 5 # y = y **5 değeri ile aynı olup y in mevcut değerini 5 kere çarparak 5 üssünü değer olarak alır.
print(x,y,z)

val = 1, 2, 3  # tuple oluştururken parantez kullanmak şart değil.
print(val)
print(type(val))

a, b, c = val #tuple listeleri bu şekilde bir değişkene atanabilir. Değişken sayısı tuple eleman sayısına eşit olmak zorunda aksi halde hata alırız.
print(a, b, c)

val2 = 1, 2, 3, 4, 5
a, b, *c = val2 # bir değişkenin başına yıldız atarak çoklu değer almasını sağlayabiliriz. Buradaki yıldız koyduğumuz c elemanı liste haline gelir.
print(a, b, *c)
print(type(c))








