# uzun yol
numbers1 = []
for x in range(10):
    numbers1.append(x)
print(numbers1)

# kısa yol
numbers = [x for x in range(10)]        # yukardaki yöntem ile aynı sonucu verir ama bu daha kısa
print(numbers)

for x in range(10):
    print(x**2)

numbers3 = [x*x for x in range(10) if x%3==0] # 1 den 10 kadar olan sayıların karelerini alır ve sadece 3 e tam bölünenleri ekrana yazdırır.
print(numbers3)

# uzun yol
myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

# kısa yol
mylist2 = [ letter for letter in myString]
print(mylist2)



years = [ 1983, 1999, 2008, 1956, 1986]
ages = [2024 - year for year in years]
print(ages)


result = [x if x%2==0 else 'TEK' for x in range(1,10)]
print(result)

# uzun yol
rs = []

for x in range(3):
    for y in range(3):
        rs.append((x,y))
print(rs)

# kısa yol
numbers4 = [(x,y) for x in range(3) for y in range(3)]
print(numbers4)