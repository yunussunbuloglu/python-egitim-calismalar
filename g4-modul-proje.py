""""""

import mymodul as mod

x1 = help(mod.func)

x = mod.number
print(x)
x = mod.numbers
print(x)
x = mod.person["name"]
print(x)
x = mod.person["age"]
print(x)
x = mod.func(10)
print(x)
p = mod.Person()
p.speak()

