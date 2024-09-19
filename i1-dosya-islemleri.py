""""""
# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erisme_modu)
# dosya_erisme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# Dosya Erişme Modları

# 'w': (Write) yazma modu. Dosyayı konumda oluşturur (Sıfırdan yazar. Önceki yazılı olanları siler)
"""oluşturulan dosya üzerinden işlemler yapabilmek için bir değişkene atadık."""
"""
file = open("newfile.txt", "w",encoding="utf-8") #encoding = utf-8 ile türkçe karakterleri tanımasını sağladık
file.write("Yunus Sünbüloğlu")
file.close()  #Dosya ile işimiz bittikten sonra dosyanın kaynakları tüketmeye devam etmemesi için dosyayı kapatmamız gerekiyor.

file2 = open("C:/users/yunus/OneDrive/Masaüstü/newfile.txt","w") #belirtilen konumda dosya oluşturmamıza yarar.
file2.close()
print(file2)
"""
# 'a': (Append) ekleme. Dosya konumda yoksa oluşturur. (Önceden yazılı olanların üzerine ekleme yaparak yazar)

file3 = open("newfile.txt", "a",encoding="utf-8")
file3.write("Yunus Sünbüloğlu")     # dosyayı her çalıştığımızda (Yunus SünbüloğluYunus SünbüloğluYunus Sünbüloğlu) şeklinde ekleme yapar.
file3.close()

# 'x': (Create) oluşturma. Dosya zaten varsa hata verir.
"""  a ve w metodlarını dosyayı oluşturur ve eğer dosya zaten varsa var olan dosyanın üzerine ekleme yapar. Eğer amacımız sadece dosya oluşturmaksa
     ve üzerine yazma ya da ekleme yapmayacaksa create ile sadece dosyayı oluştururuz ve dosya zaten mevcut ise hata vermesini sağlarız."""

file4 = open("newfile2.txt", "x",encoding="utf-8")

# 'r': (Read) okuma. varsayılan. Dosya konumda yoksa hata verir.

file4 = open("newfile2.txt", "r",encoding="utf-8")