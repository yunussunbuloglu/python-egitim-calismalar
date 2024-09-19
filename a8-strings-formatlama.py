name = "Yunus"
surname = "Sünbüloğlu"
age = 29

print("My name is {} {}and I am {} years old.".format(name,surname,age)) 
"""
    Süslü parantez içerisine yazdırmak istediklerimizi sırasıyla format ile yazılır. 
    age değişkeninde tür değişimi yapmamıza gerek kalmadı. 
    Default olarak eklediğimiz her süslü parantez 0,1,2 gibi indexli gelir.
    O yüzden formatın içine yazdığımız sıra ile ekler. Eğer değişiklik yapmak istersek
    süslü parantez içerisine ya değişken ismi ya da index numarası vermemiz lazım.
"""

result = 200/700
print("The result is {}".format(result)) # 0.2857142857142857 şeklinde sonuç verir.
print("The result is {r:1.3}".format(r=result)) # Süslü parantez içerisindeki 1 noktadan önceki basamak sayısını 3 noktadan sonraki basamak sayısını belirler.
# Süslü parantez içerisine result u direkt yazdığımızda hata veriyor o yüzden tek harflik bir tanımlama yaptık.

# FSTRİNG İFADESİ
# formattan daha kullanışlı ama ikisinide bilmekte fayda var.

print(f"My name is {name} {surname} and I am {age} years old.") 

