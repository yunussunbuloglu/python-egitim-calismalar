x, y, z = 2, 5, 10

num = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız iki değer ile x,y,z toplamının farkı kaçtır.?

a = int(input('1. Sayıyı giriniz: '))

b = int(input('2. Sayıyı giriniz: '))

t1 = x + y + z
t2 = a * b

snc = t2 - t1

print(snc)

# 2- y'nin x'e kalansız bölümünü hesaplayınız

a2 = y // x
print(a2)

# 3- (x,y,z) toplamının mod 3 ü nedir?

a3 = t1 % 3
print(a3)

# 4- y'nin x.ci kuvvetini hesaplayınız

a4 = y ** x
print(a4)

# 5- x, *y, z = num işlemine göre z nin küpü kaçtır?

x, *y, z = num
a5 = z ** 3
print(a5)

# 6- x, *y, z = num işlemine göre y nin değerler toplamı kaçtır?

x, *y, z = num
a6 = y[0] + y[1] + y[2]
print(a6)