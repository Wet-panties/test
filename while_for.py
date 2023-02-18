# from func import SumSQ
d = {'FName': 'Borka', 'LName': 'Ivanov', 'Age': 69}
# z = SumSQ(d['Age'], (d['Age'] - 1), d['FName'], 1)
# print(f'Hellow {name}, твою мать ебали {z} раз')

'''for di in d:
    print(di + ' - ' + str(d[di]))

print(d.items())

for di, v in d.items():
    print(di + ' - ' + str(v))

for di in d.keys():
    print(di)
for v in d.values():
    print(v)'''

'''from collections import namedtuple

Phonk = namedtuple('Phonk', 'NameG, NameS, NameP')
Phonk = [Phonk('Gay', 'Serge', 'Pidor'), Phonk('wluha', 'shmara', 'tvarina')]

for p in Phonk:
    print(p.NameG, p.NameS, p.NameP)'''


'''digitals = range(20)
print(digitals)

for d in digitals:
    if d == 0:
        continue
    if d % 2 == 0:
        print(f'исло {d} чётное, пропустили.')
        continue

    if d > 10:
        print(f'число {d} больше 10. прервал.')
        break
    print(f'исло {d} нечётное, возвёл в квадрат.')
    print(d**2)'''


'''list = ['One', 'Two', 3, 4.5, True, None, 'IM CUM!']

for a in list:
    print(a)'''


'''age = 10
age = int(input('Сколько те лет?:   '))
while age < 21:
    print(f'Тебе {age}? '
          f'Oh, im fucking cumming!')
    age = age + 1

print('End!')'''