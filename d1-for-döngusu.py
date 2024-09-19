numbers = [1,2,3,4,5]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

for num in numbers:         # döngü ifadesinin yanına num adında bir değişkn oluşturduk.
    print(num)              # yukarıda tektek yazdığımızı tek satırda yazmamızı sağladı.
    print('Hello')          # liste eleman sayısı kadar ekrana hello yazar.

names = ['yunus', 'rabia', 'emre', 'cennet']

for name in names:
    print(f'Hello my name is {name}')   # listedeki her eleman için tekrar döner ve yazıyı yazar.

x = 'Yunus Sünbüloğlu'

for y in x:
    print(y)            # str ifadenin her bir harfinin alt alta yazar.

tuple = [(1,2),(1,3),(3,4),(4,5)]

for t in tuple:
    print(t)        # bu şekilde parantez içindeki ikilileri bir eleman olarak algılar ve ekrana öyle yazar.

tuple1 = [(1,2),(1,3),(3,4),(4,5)]

for a,b in tuple1:
    print(a)        # bu şekilde parantez içindekilerin ilk sayılarını alır
    print(a,b)      # bu şekilde parantez içindekileri yan yana yazar ama parantez içine almaz

d1 = {'k1':1, 'k2':2, 'k3':3}

for item in d1:
    print(item)     # bu şekilde sade key bilgilerini (k1,k2,k3) yazdırır

d2 = {'k1':1, 'k2':2, 'k3':3}
for item in d2.items():
    print(item)     # bu şekilde liste elemanı gibi ikili olarak alır.

d3 = {'k1':1, 'k2':2, 'k3':3}
for key,value in d3.items():    # bu şekilde key ve value değerlerini ayrı ayrı tutabiliriz
    print(key)                  # bu şekilde sadece key bilgilerini yazdırırız
    print(value)                # bu şekilde sadece value değerlerini yazdırırız
    print(key, value)           # bu şekilde ise hem key hem value değerlerini yazdırırız.