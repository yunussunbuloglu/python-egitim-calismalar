#class
from traceback import print_tb


class Person:           # içerisine attributes ve methods tanımlamamıza yarayan kütüphane

    # class attributes
    address = 'no information'

    # constructor (Yapıcı Metod)

    def __init__(self,name,year):  # self classtan türetilen her hangi bir objeyi temsil ediyor.

        # object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı')

    # instance methods

    def intro(self):
        print('Hello There I am '+ self.name)

    def calculateAge(self):
        return 2024 - self.year


p1 = Person('yunus', 1995)
p2 = Person('rabia',1993)

p1.intro()
p2.intro()
print(f"adım: {p1.name} ve yaşım {p1.calculateAge()}")
print(f"adım: {p2.name} ve yaşım {p2.calculateAge()}")




#instance (Object)

p1 = Person('yunus', 1995)
p2 = Person('rabia',1993)



# updating  class içerisindeki objeleri güncelleyebiliriz

p1.name = 'Emre'
p1.address = 'Gonya'



# accessing object attributes

print(f"P1: name: {p1.name} year: {p1.year} address: {p1.address}")
print(f"P2: name: {p2.name} year: {p2.year} address: {p2.address}")

print(p1)
print(p2)
print(type(p1))
print(type(p2))

class Circle:
    pi = 3.14 # Class Object Attributes

    def __init__(self, yaricap=1):
        self.yaricap=yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)

c1 = Circle() # yarıçap belirtmediğimiz için 1 olarak kabul edecek
c2 = Circle(5)

print(f"c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}")
print(f"c2: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}")