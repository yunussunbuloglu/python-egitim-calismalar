""""""
"""
    ** with fonksiyonu ile açtığımız dosya with bloğunun içerisindeki kodları tamamlayınca otomatik olarak kapanır
       bu yüzden file.close dememize gerek kalmaz.
    ** as file diyerek open işlemini file isminde bir değişkene atamış oluyoruz.
"""

with open("newfile.txt","r",encoding="utf-8") as file:
    x = file.read()
    print(x)

    file.seek(0)          # imleci parantezin içerisindeki değere gönderir.

    print(file.tell())    # imlacin mevcut konumunun vermiş olur. Bu örnekte imleç 61. byte da yani 61 karakterli dosya okudu.

    x2 = file.read()
    print(x2)