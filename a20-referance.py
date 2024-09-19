# value types

x = 5
y = 25

x = y 

y = 10

print (x, y)

"""
    Kodlar satır satır gittiği için ilk başta x = y yaparak y nin 25 olan 
    ilk değeri x e atanır. Atama işleminden sonra y değerini değiştirdiğimizde 
    x e tekrar bir atama olmadığı için x  il değerini almaya devam eder.

    *** Yukardaki işleme value types denir ve str, int ve float değerlerde geçerlidir.***

"""

# referance types => list 

a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a,b)

"""
    listeler aynı adreste tutulduğu için value typelardan farklı olarak ilerleyen satırlarda farklı değerler
    atandığında iki listede de işikliği göreceğiz.

"""