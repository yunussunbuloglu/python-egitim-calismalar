x = 7
hak = 5
devam = 'e'

a = 5 < x < 10
print(a)

# and operatörü
# true - true = true
# true - false = false

a2 = x > 5 and x < 10
print(a2)

a3 = (hak > 0) and (devam == 'e')
print(a3)

# or operatörü
# true - true = true
# true - false = true
# false - false = false

a4 = (x > 0) and (x % 2 == 0)
print(a4)                       # False

a5 = (x > 0) or (x % 2 == 0)
print(a5)                       # True


# not operatörü

a6 = not (x > 0)                # normalde true dönen bir değeri False olarak değiştirir.
print(a6)


# x 5 ve 10 arasında olan bir çift sayı mı?

a7 = ((x > 5) and (x < 10)) and (x % 2 == 0)
print(a7)
