# elimizde bir liste yoksa 1-100 arası sayıları listeye almak istersek

x = 0

while x < 100:          # while true şeklinde kullanırsak sonsuz döngüye girer.
    print(x)
    x += 1
print('Döngü bitti.')

x2 = 1

while x2 <= 100:          
    if x2 % 2 == 0:
        print(f'Sayı çift {x2}')
    else:
        print(f'sayı tek {x2}')
    x2 += 1
print('Döngü bitti.')

name = '' # bu değer while döngüsünde FALSE değer verecek.

# name değeri boş olduğu için false değer verir ve döngüye girmez. o yüzden not ile true ya çevirdik.
# # Kullanıcı boşluk karakterine basarsa bunu değer olarak algılayacağından döngü biter strip() metodu ile bunu engellemiş oluyoruz.

while not name.strip():
    name = input('isminizi giriniz: ')
print(f'Merhaba {name}')