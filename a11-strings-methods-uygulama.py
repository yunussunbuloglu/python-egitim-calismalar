website = "http://www.yunussunbuloglu.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- ' Hello World ' karakter disinin baş ve sondaki boşluk karakterlerini silin                        => strip

x = ' Hello World '
x = x.strip()

# 2- 'www.yunussunbuloglu.com' içindeki yunussunbuloglu bilgisi haricindeki tüm karakterleri silin      => split

x1 = 'www.yunussunbuloglu.com'
x1 = x1.split('.')
x1 = x1[1]


# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın                                    => lower

x2 = course.lower()

# 4- 'website' içinde kaç tane u karakteri vardır. (count(a))                                           => count

x3 =website.count('u')
# website.count('u',0,10) şeklinde yazarsak 0 ile 10 indeks aralığında u harfinin kaçtane olduğunu gösterir.

# 5- 'website' www ile başlayıp .com ile bitiyor mu?                                                    => statrswith endswith

x4 = website.startswith('www')
x5 = website.endswith('com')

# 6- 'website' içinde .com iafdesi var mı?                                                              => find

x6 = website.find('.com')
# website.find('u',0,10) şeklinde yazarsak 0 ile 10 indeks aralığında u harfinin index numarasını gösterir.
# .rfind() metodu ile sayma işlemine sondan başlabilir.
# alternatif olarak .index() metodu da kullanlıbilir. rindeks() ile sondan başlatır.

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)                             => isalpha

x7 = course.isalpha()
x8 = course.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyin                 => center

x9 = 'Contents'
x9 = x9.center(50, '*')

# 9- 'course' karakter dizisindeki tüm boşlukları '-' ile değiştirin.                                   => replace

x10 = course.replace(' ', '-')

# 10- ''Hello world' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin                     => replace

x11 = 'Hello World'
x11 = x11.replace('World', 'There')

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın                                         => split

x12 = course.split()

print(x)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)
print(x8)
print(x9)
print(x10)
print(x11)
print(x12)