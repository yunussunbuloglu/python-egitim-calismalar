""""""
# Error Handling => Hata Yönetimi
try:                                    # hataları kontrol edeceğimiz blok
    x = int(input("x: "))
    y = int(input("y: "))

    print(x/y)
except ZeroDivisionError:               # hata gelmesi durumunda kullanıcıya vereceğimiz mesajları yazdığımız blok
    print("y değerine 0 girilemez")
except ValueError:
    print("x ve y için sayısal değer girmelisiniz")

"""
    except (ZeroDivisionrror, ValueError): şeklinde ortak sonuç verecek şekilde gruplandırılabilir.
    except (ZeroDivisionrror, ValueError) as e: şeklinde ortak sonuç verecek haataları bir isimlendirme yapılabilir.
    except : şeklinde tüm olası hataları kapsayarak genel olarak bir cevap vermemizi sağlar.
"""

try:
    a = int(input("a: "))
    b = int(input("b: "))

    print(a/b)
except:
    print("yanlış değer girdiniz")
else:
    print("Herşey yolunda")

"""
    yukarıdaki gibi kullanılarak kullanıcı yanlış bilgi girdiğinde hatalı değer girdiniz, doğru bilgi girdiğinde ise 
    herşey yolunda mesajı verilebir.
"""

while True:
    try:
        a1 = int(input("a1: "))
        b1 = int(input("b1: "))

        print(a1/b1)
    except:
        print("yanlış değer girdiniz")
    else:
        break
"""
    yukarıdaki gibi kullanılarak kullanıcı yanlış bilgi girdiğinde hatalı değer girdiniz mesajı verir ve kullanıcı 
    doğru bilgi girene kadar program yeniden çalışır. Kullanıcı doğru bilgi girdiğinde break ile karşılaşır ve döngüden çıkar.
"""

while True:
    try:
        a2 = int(input("a2: "))
        b2 = int(input("b2: "))

        print(a2/b2)
    except Exception as ex:
        print("yanlış değer girdiniz", ex)
    else:
        break
"""
    yukarıdaki gibi kullanılarak kullanıcı yanlış bilgi girdiğinde hatalı değer girdiniz mesajı verir ve yanında hatanın 
    neden kaynaklandığını (ZeroDivisonErrors mu ValueError mu verdiğini) göserebiliriz. While döngüsünden dolayı kullanıcı 
    doğru bilgi girene kadar program yeniden çalışır. Kullanıcı doğru bilgi girdiğinde break ile karşılaşır ve döngüden çıkar.
"""

while True:
    try:
        a2 = int(input("a2: "))
        b2 = int(input("b2: "))

        print(a2/b2)
    except Exception as ex:
        print("yanlış değer girdiniz", ex)
    else:
        break
    finally:
        print("try except sonlandı")
"""
    yukarıdaki gibi kullanırsak finally, except çalışsada çalışmasada her zaman çalıştırılır. 
    Kullanım amacı ise açılan dosyanın kapatılması ve atanan değişkenlerin silinmesi içindir.
"""
