"""
    Dictionary ler key - value şeklinde çalışır.
    {41, kocaeli 
    34, istanbul}
    şehirlere ulaşmak için plakaları kullanabiliriz.
    bu işlem listelerden de yapılabilir ama çok karmaşık ve uzun bir işlem olur.

"""

plakalar = { 'kocaeli' : 41, 'istanbul' : 34 }

print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['ankara'] = 6 # dictionary e yeni bir key : value bilgisi eklenmiş olur.
print(plakalar)

plakalar['kocaeli'] = 'new value' # 'kocaeli' keyinin value su değişmiş oldu.
print(plakalar)


users = {
    'yunussunbuloglu': {
        "age": 29,
        "roles": 'user',
        "email": 'ys@gmail.com',
        "address": 'gonya',
        "phone": '123123123'
    },
    'rabiasunbuloglu':{
        'age': 31,
        'roles': ['admin','user'],
        'email': 'rs@gmail.com',
        'address': 'gonya',
        'phone': '321321321'
    }
}
print(users['rabiasunbuloglu'])
print(users['rabiasunbuloglu']['age'])
print(users['rabiasunbuloglu']['email'])
print(users['rabiasunbuloglu']['address'])
print(users['rabiasunbuloglu']['roles'])
print(users['rabiasunbuloglu']['roles'][0])



