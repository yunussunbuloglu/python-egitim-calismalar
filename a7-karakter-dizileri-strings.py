name = "Yunus"
surname = "Sünbüloğlu"
age = 29

print("My name is "+ name + " " + surname + " and \nI am " + str(age) + " " + "years old.") # age değişkeni int olduğu için + ile eklerken hata alınır o yüzden str ye dönüştürdük.


# Stringler liste gibi davranır her bir karakteri ifade eden index numarası var.
# len() komutu listenin son indexi 

print(name[0]) # name isimli değişkenin 0 numaralı indexi olan Y harfini yazdırır.
print(name[1]) # name isimli değişkenin 1 numaralı indexi olan u harfini yazdırır.
print(name[2]) # name isimli değişkenin 2 numaralı indexi olan n harfini yazdırır.
print(name[3]) # name isimli değişkenin 3 numaralı indexi olan u harfini yazdırır.
print(name[4]) # name isimli değişkenin 4 numaralı indexi olan s harfini yazdırır.
print(len(name)) # name isimli değişkenin kaç karakterli olduğunu yani listenin uzunluğunu yazdırır.
print(name[len(name)-1]) # name isimli değişkenin son indexli karakterini yazdırır.
print(name[-1]) # name isimli değişkenin son indexli karakterini yazdırır.

print(name[1:3]) # name isimli değişkenin 1. indexten 3. indexe kadar olan kısmı yazdırır. => !!! 3. index yazılmaz !!! <=
print(name[2:]) # name isimli değişkenin 2. indexten son indexe kadar olan kısmı yazdırır.
print(name[:4]) # name isimli değişkenin 0. indexten 4. indexe kadar olan kısmı yazdırır. => !!! 4. index yazılmaz !!! <=
print(name[1:4:2]) # name isimli değişkenin 1. indexten 4. indekse kadar 2 şer artacak şekilde yazar.


