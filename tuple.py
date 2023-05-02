from collections import namedtuple
info = namedtuple('information', 'Name, Properties, Age, IsLover')
info = [info('Ксюша', 'моя любимая сладкая жопка', 19, True), info('Пата', 'глупая жопка', 25, True)]
print(info)
name = info[0].Name
print(name)


'''info = ('Ксюша', 'любимая сладкая жопка', 19, True)
print(info)
print(type(info))

print(info[0])

print(info[1])
print(info[2])
print(info[3])
firstname, properties, age, isLove = info
print(firstname, properties, isLove)

'''