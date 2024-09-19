
# range() metodu

for item in range(50,100,20):
    print(item)                     # range ile 50 den başlayıp 100 e kadar 20 şer artan bir dögü oluşturur

print(list(range(50,100,20)))       # range ile 50 den başlayıp 100 e kadar 20 şer artacak şekilde oluşturulan döngüyü liste içine alarak ekrana yazar.


# enumerate() metodu

index = 0
greeting = "Hello"

for letter in greeting:
    print(f"index: {index} letter: {letter}")
    index += 1

greeting = "Hello"

for index,letter in enumerate(greeting):            # Yukarıda yaptığımız ile aynı sonucu verir.
    print(f"index: {index} letter: {letter}")

greeting = "Hello"

for item in enumerate(greeting):                    # Yukarıda yki gibi yazmaz ama (0, 'H') şeklinde tüm indexi ve karakteri parantez içinde verir.
    print(item)

# zip() metodu

# aynı indexteki elemanları tuple elemanı olarak birleştirir.
# eleman sayıları eşit olmak zorunda örneğin list1 den 5 i silersek 1,2,3,4 için birleştirir 5 in indexindeki elemanları birleştirmez.

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100,200,300,400,500]
print(list(zip(list1, list2,list3)))

for item in zip(list1, list2,list3):
    print(item)