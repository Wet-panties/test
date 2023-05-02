l = {'ксюша': 'умняшка', 'паша': 'дулак'}

s = l['ксюша']
p = l['паша']
print(s,p)

l['жопа'] = 'пата'

print(l['жопа'])

print(l)

print(l.keys())
print(l.values())

'''print(l.get('ксюша'))
a = l.pop('жопа')
print(a)'''

l.update({'пата': 'зопа'})
print(l)