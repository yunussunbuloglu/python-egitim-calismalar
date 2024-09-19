website = "http://www.yunussunbuloglu.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır.

print(len(course)) # 65 karakter var.

# 2- 'website' içinden www karakterlerini alın.

print(website[7:10])

# 3- 'website' içinden com karakterlerini alın.

print(website[-3:]) 

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.

print(course[:16])
print(course[-15:])

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

print(course[::-1]) # [::] ifadesi listenin tüm elemanlarını yazdırır. Sondaki -1 de dizdeyi tersten yazdırır. Normalde oraya 2 yazarsak 2 karkterde bir yazdırır.

#**********************************************************************************************************************************************************************

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

# 6- Yukarıda verilen değişkenler ile ekrana "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis." yazdırın

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

# 7- 'Hello world' ifadesindeki w harfini W ile değiştirin

b0 = 'Hello world'
b1 = b0[0:6] + 'W' + b0[-4:]
b0.replace('w', 'W') # replace metodu ile de yapılabilir.

print(b1)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın

c = 'abc ' * 3
print(c)

