mylist = [1,2,3]
mystring = 'my string'

print(len(mylist))
print(len(mystring))
print(type(mylist))
print(type(mystring))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration     # normalde bunu yapmazsak len metodu hata verir ama şimdi filmin süresini ekrana yazar

    def __del__(self):
        print("Movie Silindi")


m = Movie('film adı', 'yönetmen adı', 120)

print(str(mylist))
print(str(m))

print(len(mylist))
print(len(m))

del m


