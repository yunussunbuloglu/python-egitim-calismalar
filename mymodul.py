""""""
"""
    Modül hakkında bilgilendirme

"""
print("Modül eklendi")

number = 10

numbers = [1,2,3]

person = {
    "name": "Ali",
    "age": "25",
    "city":"İstanbul"
}

def func(x):
    """
        fonksiyon hakkında bilgilendirme
    :param x: x
    :return: print
    """
    print(f"x: {x}")

class Person:
    def speak(self):
        print("I am speaking...")