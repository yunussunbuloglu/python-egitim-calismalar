""""""
import re

# raise: kendi hatalarımız oluşturmak için kullanılır.
"""
    x = 10
    
    if x > 5:
        raise Exception("x 5 den büyük değer alamaz.")

"""

def check_password(psw):
    if len(psw) < 8:
        raise Exception("Parola en az 7 karakterli olmalıdır.")
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam içermelidir.")
    elif not re.search("[_@$]", psw):
        raise Exception("parola alpha numerik karakter içermelidir.")
    elif re.search(" ", psw):
        raise Exception("parola boşluk içermemelidir.")
    else:
        print("Geçerli Parola")

password = "12345678aA_"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli Parola: Elseden gelen")
finally:
    print("validation tamamlandı.")



class Person:
    def __init__(self, name, yaer):
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter içeriyor")
        else:
            self.name = name

p = Person("Yunuuuuuuuuuuuuuuusss", 1995) # Exception: Name alanı fazla karakter içeriyor şeklinde hata alır.