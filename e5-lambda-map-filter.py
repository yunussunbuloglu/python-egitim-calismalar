def square(num): return num ** 2    # bu şekilde kısa kullanım yapılabiliyor

numbers = [1, 3, 5, 9, 4, 10]

result = square(2)

print(result)

# map

def square2(num2): return num2 ** 2    

numbers2 = [1, 3, 5, 9]

result2 = list(map(square2,numbers2))   
"""
    map metodunu kullanırken fonksiyonun sadece adını ve listenin adını yazarız.
    map metonundan dönen değerleri görebilmek için map metodunuda bir liste için aldık
"""
for item in map(square, numbers):  # yukardaki yönteme alternatif bir yöntem
    print(item)

# Lambda 
"""
    Lambda ile tek kullanımlık fonksiyonlar yapılır.
"""

numbers2 = [1, 3, 5, 9]

result3 = list(map(lambda num: num ** 2,numbers2))  
print(result3)

# Filter
"""
    Filter ile fonksiyondan geri dönmesini istediğimiz sonuçları filitreleyebiliriz. Sadece çiftleri döndür gibi...
"""
def check_even(num3): return num3 % 2 == 0

x = list(filter(check_even, numbers))

print(x)