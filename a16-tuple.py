list = [1, 2, 3]

tpl = (1, 'iki', 3)

print(type(list))
print(type(tpl))

print(list[2])
print(tpl[2])

print(len(list))
print(len(tpl))

list = ['Ali', 'Veli']  # tüm listeyi siler yeniden liste oluşturur
tpl = ('damla', 'ayşe') # tüm tuple ı siler yeniden tuple oluşturur

print(list)
print(tpl)

list[0] = 'ahmet' # direkt bir elemanı silip yerine yeniden eleman atamak istersek liste sorunsuz çalışır.
#tpl[0] = 'deniz' # direkt bir elemanı silip yerine yeniden eleman atamak istersek tuple hata verir

print(list)
print(tpl)

"""
    Tuple da sadece tüm listeyi değiştirmek istersek atama yapılabilir. Belirli bir indexe yeni atama yapılamaz.
    sadece .count() ve .index() metodu kullanılabilir.
    
"""