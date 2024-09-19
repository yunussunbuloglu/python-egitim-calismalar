liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

""" *** 1- Liste elemanları içindeki sayısal değerleri bulun."""

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue            # Bulduğu her ValueeError için continue den dolayı atlayıp hatasız değerleri yazdı.

""" *** 2- Kullanıcı q değerini girmedikçe aldığınız her inputun sayı
          olduğundan emin olunuz aksi halde hata mesajı yazın. """


while True:
    sayi = input("Sayı: ")
    if sayi == "q":
       break
    try:
        result = float(sayi)
        print("girdiğiniz sayı", result)
        break
    except:
        print("geçersiz sayı")
        continue


""" *** 3- Girilen parola içindeki türkçe karakter hatası veriniz.  """


def checkPassword(parola):

    turkce_karakter = "şŞçÇğĞüÜöÖıİ"

    for i in parola:
        if i in turkce_karakter:
            raise TypeError("Parola Türkçe Karakter İçeremez.")
        else:
            pass

    print("Geçerli Parola")

parola = input("Parola: ")

try:
    checkPassword(parola)
except TypeError as err:
    print(err)

""" *** 4- Faktöriyel fonksiyonu oluşturup fonksyona gelen değer için
           hata mesajları verin.  """

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif değer")

    result = 1

    for i in range(1, x+1):
        result *= i

    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)