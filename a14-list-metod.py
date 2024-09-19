numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

x = min(numbers) # sayısal olarak minimum değeri yazar
print(x)

x1 = max(numbers) # sayısal olarak maximum değeri yazar
print(x1)

x2 = min(letters) # alfabetik olarak ilk değeri yazar
print(x2)

x3 = max(letters) # alfabetik olarak son değeri yazar
print(x3)

numbers[4] = 40 # 4. indexteki elemanı 40 olarak günceller.
print(numbers)

numbers.append(333) # listenin sonuna parantez içine yazılan değeri ekler.
print(numbers)

numbers.insert(3, 78) # 3. indexe 78 sayısını ekler ve diğer elemanları sağa doğru kaydırır
print(numbers)

numbers.insert(-1, 52) # sondan bir önceki sıraya ekler. En sona eklemez. Son elemanı sağa kaydırdığı için sondan bir önceki indexe ekler.
print(numbers)

numbers.pop() # default olarak -1. index gelir ve listenin son elemanını siler. Parantez içerisine index değeri girilirse o indexteki elemanı siler.
print(numbers)

numbers.remove(1) # silmek istediğimiz karakteri parantez içerisine yazarsak listeden o elemanı siler.
print(numbers)

numbers.sort() # sayısal dizileri küçükten büyüğe sıralar
letters.sort() # alfabetik dizileri alfabeye göre sıralar

print(numbers)
print(letters)

numbers.reverse() # listeyi ters çevirir.
letters.reverse() # listeyi ters çevirir.
print(numbers)
print(letters)

print(len(numbers)) # listede kaç eleman olduğunu verir
print(len(letters)) # listede kaç eleman olduğunu verir

print(numbers.count(10)) # parantez içerisindeki değeri listede sayar ve adedini verir.
print(letters.count(10)) # parantez içerisindeki değeri listede sayar ve adedini verir.

