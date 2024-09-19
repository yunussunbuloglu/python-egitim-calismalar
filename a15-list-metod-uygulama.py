names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyin.

names.append('Cenk')
print(names)

# 2- "Sena" değerini listenin başına ekleyin.

names.insert(0,'Sena')
print(names)

# 3- Deniz isminin indexi nedir

x = names.index('Deniz')
print(x)

# 4- Deniz ismini listeden silin

names.remove('Deniz')
print(names)

# 5- "Ali" listenin bir elemanı mıdır)

print('Ali' in names)

# 6- liste elemanlarını ters çevirin

names.reverse()
print(names)

# 7- liste elemanlarını alfabetik sırala

names.sort()
print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayın

years.sort()
print(years)

# 9- str = "Chevrolet,Daica" karakter dizisini listeye çevirin

str = "Chevrolet,Daica"
x = str.split(',')
print(x)

# 10- years dizisinin en büyük ve en küçük elemanı nedir

eb = max(years)
print(eb)

ek = min(years)
print(ek)

# 11- years dizinde kaç tane 1998 değeri vardır?

x = years.count(1998)
print(x)

# 12- years dizisinin tüm elemanlarını siliniz.

years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []
x = input('1.Marka: ')
markalar.append(x)
x = input('2.Marka: ')
markalar.append(x)
x = input('3.Marka: ')
markalar.append(x)

print(markalar)



