# identity (is) operatörü
# referans kontrolü yapar. içeriği aynı olsa bile objeler aynı adreste tanımlı değilse False değer döner

x = y = [1,2,3]
z = [1,2,3]

print(x == y)       # True
print(x == z)       # True
print(x is y)       # True
print(x is z)       # False

# Membership (in) operatörü
# Sorduğumuz bir bilginin liste içinde olup olmadığını kontrol eder.

x2 = ['apple', 'banana']
print('banana' in x2)   #True

name = 'yunus sunbuloglu'
print('u' in name)