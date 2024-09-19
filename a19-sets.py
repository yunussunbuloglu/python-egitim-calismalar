"""
    liste içerisinde olan bir elemanı eklemeye çalışırsak eklemez ama hata da vermez

"""

fruits = {'orange', 'apple', 'banana'}

print(fruits)
# print(fruits[0]) şeklinde kullanılamaz çünkü setlerde indexleme yoktur. Sırasızdır.

for x in fruits:  # döngü ile elemanları alt alta yazdırılabilir.
    print(x)

fruits.add('cherry')    # set listesinin içerisinde random bir yere ekleme yapar.
print(fruits)

fruits.update(['mango', 'grape'])   # set içerisinde karışık bir şekilde ekler
print(fruits)

fruits.remove('mango')
print(fruits)

fruits.discard('apple')
print(fruits)

fruits.pop()        # normalde son elemanı siler ama setler sıralı olmadığı için o an son eleman hangisi ise onu siler yani random silmiş olur.
print(fruits)
