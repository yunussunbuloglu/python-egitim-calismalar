name = 'Yunus'

for letter in name:
    if letter == 'u':
        break                           # Döngüden tamamen çıkar
    print(letter)

name2 = 'Yunus'

for letter1 in name2:
    if letter1 == 'u':
        continue                        # Sadece işeretlediğimiz alanı yazmaz ama döngüye devam eder.
    print(letter1)

x = 0 

while x < 5:
    if x == 2:
        break                             # 2 ye kadar yazar 2 den sonra döngüden çıkar
    print(x)
    x += 1

while x < 5:
    x += 1
    if x == 2:
        continue                           # 2 ye kadar yazar 2 den sonra döngü 2 de takılı kalacağı için x += 1 ifadesini if bloğundan önce yazmamız gerekiyor. Sadece 2 yi yazmaz.
    print(x)

# 1-100 arası tek sayıların toplamı

dx = 0
toplam = 0

while dx <= 100:
    dx += 1
    if dx % 2 == 0:
        continue
    toplam += dx
print(f"Toplam: {toplam}")

