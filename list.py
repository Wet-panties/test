l = [1, 'петух', 1.4, ['дом', 'jopa', 'govno']]
print(l)


five = l[1]
print(five)

s = l[3]
print(s)

s1 = l[3][1]
print(s1)

l[3].append('zalupa')
print(l)

l.insert(2, '123')
print(l)

l.pop(2)
print(l)

l.remove('петух')
print(l)

l2 = l.copy()

print(l2)

l3 = l + l2
print(l3)


c = l3[2].count('jopa')
print(c)

