
os = {'Windows', 'MacOS', 'RedOS', 'CentOS'}
print(os)
osnew = {'Windows', 'RedOS'}

osall = os.union(osnew)
print(osall)
'''соединяет os и osnew ез повторений '''

os1 = os.intersection(osnew)
print(os1)
'''выведет только повторяющиеся из os и osnew'''

os2 = os.difference(osnew)
'''выведет только отличабщиеся в os из osnew'''
print(os2)

os3 = osnew.difference(os)
'''выведет только отличабщиеся в osnew из os'''
print(os3)





z = os.issubset(osnew)
print(z)
'''тру или фолс содержит ли osnew всё то же, что и os'''
x = os.issuperset(osnew)
print(x)
'''тру или фолс НЕсодержит ли osnew всё то же, что и os'''


ws = frozenset({'WinOS', 'RedOS', 'MacOS'})
wsnew = frozenset({'WinOS', 'RedOS', 'MacOS', 'SteamOS'})
print(ws)
print(type(ws))
print(wsnew)
print(type(wsnew))

a = 1

ws1 = ws.union(wsnew)
print(ws1)

'''os1 = set()'''

'''.add .remove .pop'''
'''
os.remove('MacOSS') выдаст ошибку
os.discard('MacOSS') не выдаст'''

