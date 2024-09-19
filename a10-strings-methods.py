message = " Hello There. My name is Yunus Sünbüloğlu"

message1 = message.upper() # upper metodu tüm karakterleri büyük harfe çevirir. 
# Biz burada message değişkenine upper metodunu uygulayarak message değişkenine yeniden atarak değişkeni güncelledik.

message2 = message.lower() # lower metodu tüm karakterleri küçük harfe çevirir. 

message3 = message.title() # title metodu tüm kelimelerin  baş harfini büyük harfe çevirir. 

message4 = message.capitalize() # capitalize metodu sadece listenin ilk harfini büyük harfe çevirir.

message5 = message.strip() # strip metodu listenin başında ve sonun varsa boşluk karakterini temizler. 
# lstrip() metodu sadece sol rstrip() mtodu ise sadece sağdaki boşluğu siler

message55 = message.lstrip('helo') # çıktı olarak message dizisinin içindeki hello karakterlerini siler. Herkarakterin tırnak içerisine bir kere yazılması yeterli.

message6 = message.split() # split metodu listeyi boşluklardan ayırarak her birini ayrı bir liste (dizi) yapar. Her elemana index ile ulaşılabilir.
# split metodunun default ayarı boşluk olarak gelir. Pazantezler içerisine bir değer girilirse o değerden parçalara ayırır.

message7 = '---'.join(message6) # join ile dize elemanlarını tek bir string ifadeye dönüştürür. tırnakların içerisine ne yazılırsa elemanları birleştirirken araya onu koyar.

message8 = message.find('Yunus') # find metodu sonrasında çıktı aradığımız kelimenin ilk harfinin index numarasınıdır. Eğer yoksa -1 olarak döner.

message9 = message.startswith(' Hello') # startswith metodu string ifadenin ne ile başladığını sorgular.
#Parantez içerisinde verilen değer ile sorgu yapar ve sonrasında True / False olarak döner.

message10 = message.endswith('Sünbüloğlu') # endswith metodu string ifadenin ne ile bittiğini sorgular.
#Parantez içerisinde verilen değer ile sorgu yapar ve sonrasında True / False olarak döner.

message11 = message.replace(' ', '-') # replace metodu string ifadesinde genel bir arama yapar. 
# Parantez içerisinde verdiğimiz ilk değeri girdiğimiz ikinci değer ile değiştirir.
# message11 = message.replace(' ', '-').replace('Yunus', 'Emre') vs gibi nokta koyarak devam edebiliriz. 

message12 = message.center(100) # parantez içerisine girdiğimiz değer kadar bir alan oluşturur ve string ifademizi bunun içine konumlandırır.
# Eğer (100, '-') şeklinde girilirse string ifadeden kalan yerlerde - işareti ile doldurur.
message13 = message.center(50,'-')
# ljust() ile aynı işlemi yazıyı sola yaslayarak yazdırabiliriz.
# rjust() ile aynı işlemi yazıyı sağa yaslayarak yazdırabiliriz.
"""
    Diğer metodları w3scholl üzerinden incelenebilir

"""

print(message)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message55)
print(message6)
print(message7)
print(message8)
print(message9)
print(message10)
print(message11)
print(message12)
print(message13)