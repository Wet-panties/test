

inet = None
print(type(inet))

connection = props(user, password, ip, port)
inet = connection.connect()
'''если в переменную придут хоть какие-то данные, то  тип None сменится на любой другой'''



if inet is None:
    print('Соси хуй')
else:
    print('Лааадно, другой раз')
