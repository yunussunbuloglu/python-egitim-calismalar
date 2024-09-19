sayilar = [1,3,5,7,9,12,19,21]

# 1- sayılar listesini while ile ekrana yazdırın

x=0
while x < 1:
    print(sayilar)
    x += 1

x = 0
while (x < len(sayilar)):
    print(sayilar[x])
    x += 1


# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

sayi1 = int(input('ilk değeri giriniz: '))
sayi2 = int(input('ikinci değeri giriniz: '))

i = sayi1
while  i < sayi2:
    if i % 2 == 1:
        print(i)
    i += 1

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın

x1 = 100

while x1 > 0:
    print(x1)
    x1 -= 1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

x2 = []


while len(x2) < 5:
    i = int(input('sayı: '))
    x2.append(i)
x2.sort()
print(x2)

# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesinde saklayın.
#    ** ürün sayısını kullanıcıya sorun
#    ** dictionry listesi yapısı (name, price) şeklinde olsun
#    ** ürün ekleme işlemi bittiğinde ürünleri ekrana yazdır.

urunler = []

adet = int(input('Kaç adet ürün eklemek istersiniz: '))

i = 0 

while i < adet:
    name = input('ürün ismi:')
    price = input('Fiyat bilgisi: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1
for urun in urunler:
    print(f"ürün adı {urun['name']} ürün fiyatı: {urun['price']}")
