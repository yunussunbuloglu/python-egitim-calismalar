# Global Scope
x = "global x"

def function():
    # Local Scope
    x = "lokal x"
    print(x)
function()
print(x)            # global x değişkenini verir eğer fonksiyonunun içinde print yaptırırsak lokal x değeri gelir. 


###################################################

name = "Yunus"

def changeName(new_name):
    name = new_name
    print(name)

changeName("Rabia")
print(name)

###################################################
# iç içe fonksiyon kullanımı

name = "Global String"

def greeting():
    
    name = "Çınar"
    
    def hello():
        
        print("hello "+ name)
    
    hello()

greeting()

###################################################

x = 50

def test():
    global x                # bu şekilde fonksiyonun içindeki x değerini lokalden globale çevirmiş oluruz.
    print(f"x : {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)


