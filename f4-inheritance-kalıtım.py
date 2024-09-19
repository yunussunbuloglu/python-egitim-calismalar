""""""
# Inheritance (Kalıtım): Miras Alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)  böylelikle student bir person ve teacher bir person olarak algılanacak.
# buna Student ve Teacher sınıfları Person sınıfını miras aldı diyebiliriz.
"""
class Person():
    def __init__(self):
        print("person created")

class Stutend(Person): # Parantez içerisinde person classını belirterek Studenta person clasının özelliklerini miraz etmiş olduk.
    def __init__(self):
        Person.__init__(self)
        print("student created")

p1 = Person()
s1 = Stutend()
"""
########################################################################################################################################

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("person created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print('I am a eating')

class Stutend(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("student created")

    # Override => fonksiyonun sınıfın içinde miras ile gelen fonksiyon ve metod ezilebilir.

    def who_am_i(self):
        print('I am a student')

    def sayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname,lname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1 = Person('Ali', 'Yılmaz')
s1 = Stutend('Çınar', 'Turan', 124)
t1 = Teacher("Serkan", "Yılmaz", "Math")

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()
s1.sayHello()