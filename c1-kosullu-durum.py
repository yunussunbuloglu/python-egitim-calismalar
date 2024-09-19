if 3 > 2:
    print('Hoş geldiniz')       # ekrana hoş geldiniz yazar

if 3 > 3:
    print('Hoş geldiniz')       # ekrana hoş geldiniz yazmaz

if True:
    print('Hoş geldiniz')       # ekrana hoş geldiniz yazar

if False:
    print('Hoş geldiniz')       # ekrana hoş geldiniz yazmaz

isLoggedin = True

if isLoggedin:
    print('Hoş geldiniz')       # ekrana hoş geldiniz yazar

username = 'ynssnbl'
password = '1234'

if (username == 'ynssnbl'):
    if (password == '1234'):
        print('Hoş Geldiniz')
    else:
        print('Parola Yanlış')
else:
    print('kullanıcı adı yanlış')