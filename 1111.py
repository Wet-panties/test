import numpy as np
import re
import random
from random import randint
from matplotlib import pyplot as plt
import math
from datetime import datetime
import time
import json
import requests
import hashlib
import sqlalchemy as sqal
import pandas


#  HW1

def hw_cycle(n: int) -> int:
    """
    Функция считает факториал целочисленного числа
    через цикл For
    """
    if n == 0:
        n = 1
    else:
        for i in range(n - 1):
            n = (i + 1) * n
    return n


#  print(hw_cycle(5))

# HW2

hw_dict = {'el0': 0, 'el1': 30, 'el2': 60, 'el3': 80, 'el4': 10, 'el5': 90}


def hw_sin(hw_dict: dict) -> dict:
    """
    Функция принимает словарь
    и высчитывает синус каждого значения
    этого словаря, а после возвращает
    копию этого списка с значениями равными
    синусом прошлых значений
    """
    for key in hw_dict:
        hw_dict[key] = np.sin(hw_dict[key] * np.pi / 180)
        #  print(key)
        #  print(hw_dict[key])
    return hw_dict


#  print(hw_sin(hw_dict))
#  print(hw_dict['el3'])
#  print(hw_sin(hw_dict))
#  hw_dict.update()
#  print(*hw_dict)
#  dct = {'el7':[7, 5, 6]}
#  print(dct)

# HW3

def random_list_3el(j, t, p: int) -> list:
    """
    Функция создает случайный список и при помощи цикла While
    удаляет в нём значения до тех пор пока не останется 3 значения.
    """
    lst = [randint(j, t) for i in range(p)]
    while len(lst) != 3:
        lst.pop()
        continue
    return lst


#  print (random_list_3el(5, 10, 20))

# HW4

def sin_cos_showoff(hw_dict: dict):
    """
    Функция принимает на вход словарь
    и выводит график sin и cos значений этого словаря
    """
    graf_sin = []
    graf_cos = []
    for key in hw_dict:
        graf_sin.append(np.sin(hw_dict[key]))
        graf_cos.append(np.cos(hw_dict[key]))
    plt.plot(graf_sin)
    plt.plot(graf_cos)
    return plt.show()


#  print(sin_cos_showoff(hw_dict))

# HW6

#  any_dict = {}
#  for i in range(5):
#      key = input()
#      value = randint(0, 999999)
#      any_dict[key] = value
#
#  with open('files/usersID.json', 'a') as uID:
#      print(any_dict, file=uID)
#      any_dict_sort = list(any_dict.keys())
#      any_dict_sort.sort()
#      for i in any_dict_sort:
#          print(i, ':', any_dict[i])
#      uID.write(uID for key in randint(0,999999))
#      print((uID for key in random.choices(population='agdgeghsdh')), file=uID)
#      dict_from_uID = {'user1':'','user2':'','user3':'','user4':'','user5':''}
#      def dict_uID_with_randint_key(dict_from_uID:dict):
#          """
#          Функция принимает словарь и с помощью
#          цикла for добавляет случайное числовое значение
#          к каждому ключу, а после запиывает этот словарь
#          в файл userID.json
#          """
#          for key in dict_from_uID:
#              dict_from_uID[key] = randint(0, 999999)
#          return dict_from_uID
#      print(dict_uID_with_randint_key(dict_from_uID), file=uID)
#      print(re.search('\w', 'files/usersID.json'))
#      print(uID.read())


# HW7

test_string = "aaa mayonez suka ketchup huy suka blyad aaa dodik MANDA MagaZin suka "


#  get_some_words_to_string = str(input())
#  test_string = test_string + get_some_words_to_string.upper()
#  print(test_string)

# HW8

def repetition_finder(test_string: str) -> list:
    """
    Функция принимает строку и считает колличество повторений слов
    далее возвращает слово и колличество его повторений
    """
    repetition = re.findall('[a-zA-Z]{,}''\s+', test_string)
    string_and_count = []
    for i in repetition:
        if i in string_and_count:
            continue
        elif repetition.count(i) >= 0:
            string_and_count.append(i)
            repetition.remove(i)
            string_and_count.append(repetition.count(i))
    return string_and_count


#  print(repetition_finder(test_string))

# HW9

a, b, c = 1, 2, 3

discriminant = lambda a, b, c: (b ** 2) - 4 * a * c
discr_res = discriminant(a, b, c)


def kvur_withdiscr(discr: int) -> np.ndarray or str:
    """
    Функция принимает на вход lambda функцию,
    и в зависимости от значения это функции
    выводит корень уравнения либо их список.
    """
    if discr < 0:
        return "Уравнение не имеет корней"
    elif discr == 0:
        x = (-b) / (2 * a)
        return x
    elif discr > 0:
        x1 = (-b + (discr) ** (0.5)) / (2 * a)
        x2 = (-b - (discr) ** (0.5)) / (2 * a)
        x = np.linspace(x1, x2)
        return x


x = kvur_withdiscr(discr_res)


def kvur_graf(x: np.ndarray, discr: int, a: int, b: int, c: int) -> None:
    """
    Функция принимает на вход х
    и результат функции discr
    являющиеся результатом функции
    kvur_withdiscr(discr) и рисует
    график квадратичного уравнения
    """
    if discr < 0:
        return
    else:
        y = a * (x ** 2) + b * x + c

        plt.plot(x, y, label=f"Корни уравнения х1 = {round(x[0], 2)}, х2 = {round(x[-1], 2)}")
        plt.ylabel("ось Y")
        plt.xlabel("ось Х")
        plt.legend()
        plt.title(f"График квадратного уравнения: {a}*x^2+{b}*x+{c}")
        #  plt.savefig("1.png")
        plt.show()


#  print (kvur_withdiscr(discr))
#  print (kvur_graf(x, discr_res, a, b, c))

# HW10

list_to_sort = [5, 3, 6, 2, 5, 6]

#  def my_sort(list_to_sort:list)->list:
for i in range(0, len(list_to_sort)):
    for j in range(i + 1, len(list_to_sort)):
        if list_to_sort[i] > list_to_sort[j]:
            list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
#  return list_to_sort
#  print(list_to_sort)

# HW SBER

black_list = [5]


#  4, 2, 0, 3, 2, 5, 0, 1
#  0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1

def waterline(black_list: list, water_list=None) -> int:
    """
    Функция принимает на вход список
    и возвращает число заполненых пустот между
    максимумов принимаемого списка
    """
    highground = []
    water_list = 0

    for i in range(len(black_list)):
        if black_list[i] != 0:
            highground.append(black_list[0])
            break
        else:
            highground.append(black_list[1])
            black_list.pop(black_list[i])
            break

    t = 0
    for i in range(1, len(black_list) - 1):
        if black_list[i] < highground[t]:
            continue
        elif black_list[i] >= highground[t]:
            highground.append(black_list[i])
            t += 1

    for i in range(1, len(black_list)):
        if black_list[-i] < black_list[-i - 1]:
            highground.append(black_list[-i - 1])
        else:
            highground.append(black_list[-i])

    c = 0

    for i in range(1, len(black_list) - 1):
        if highground[c + 1 - len(highground)] == black_list[i]:
            c += 1
        elif highground[c - len(highground)] > highground[c + 1 - len(highground)]:
            c += 1
            water_list += highground[c - len(highground)] - black_list[i - len(black_list)]
        else:
            water_list += highground[c - len(highground)] - black_list[i]
    return water_list


#  print(waterline(black_list))

# HW 11

def divide_in_percent(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if (result * 100) < 0:
            return "Числа должны быть положительные"
        elif (result * 100) > 100:
            return 100
        elif (result * 100) >= 0 or (result * 100) <= 100:
            return result * 100
        return result

    return wrapper


@divide_in_percent
def divide(a: int, b: int) -> float:
    """
    Делит 2 числа
    """
    return (a / b)


#  print (divide(5, 8))

# HW 12
# HW 12.1 (моя сортировка(похожа на сортировку вставками))

time_test1 = """
list_to_sort = [9,2,7,1,3,6,9,0,1,5,4,7,9]
for i in range(0, len(list_to_sort)):
    for j in range(i+1, len(list_to_sort)):
        if list_to_sort[i] > list_to_sort[j]:
            list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
"""
# ~8-10 sec
#  print(timeit.timeit(time_test1))

# HW 12.2 (ортировка вставками)

time_test2 = """
my_list = [9,2,7,1,3,6,9,0,1,5,4,7,9]
for i in range(1,len(my_list)):
    top = i-1
    while top:
        if my_list[top]<my_list[top-1]:
            my_list[top-1],my_list[top]=my_list[top],my_list[top-1]
        top-=1
"""
# ~8-8.5 sec
#  print(timeit.timeit(time_test2))

# HW 12.3 (Сортировка методом выбора)

time_test3 = """
my_list = [9,2,7,1,3,6,9,0,1,5,4,7,9]
for i in range(len(my_list)-1):
    for j in range(i+1, len(my_list)):
        if my_list[j]<my_list[i]:
            my_list[i],my_list[j]=my_list[j],my_list[i]
"""
# ~8-9 sec
#  print(timeit.timeit(time_test3))

# HW 12.4 (Сортировка пузырьками)

time_test4 = """
my_list = [9,2,7,1,3,6,9,0,1,5,4,7,9]
for i in range(1,len(my_list)):
    for j in range(0,len(my_list)-i):
        if my_list[j]>my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
"""
# ~10-11 sec
#  print(timeit.timeit(time_test4))

# HW 12.5 (Быстрая сортировка - сортировка Тони Хоара)

time_test5 = """
my_list = [9,2,7,1,3,6,9,0,1,5,4,7,9]
def quick_sort(array:list)->list or None:
    if len(array)<=1:
        return
    barrier=array[0]
    L=[]
    M=[]
    R=[]
    for elem in array:
        if elem<barrier:
            L.append(elem)
        elif elem==barrier:
            M.append(elem)
        else:
            R.append(elem)
    quick_sort(L)
    quick_sort(R)
    k=0
    for i in L+M+R:
        array[k]=i
        k+=1
    return array
"""
# ~0.2 sec
#  print(timeit.timeit(time_test5))

# HW 13

#  in_count = [i for i in range(int(input())+1)]
#
#  for i in in_count:
#      for j in range(1, len(in_count)):
#          in_count[j], in_count[j+1 - len(in_count)] = in_count[j+1 - len(in_count)], in_count[j]
#          print(in_count)

# HW 14


# HW 15


# HW 16

list1_to_zip = [1, 2, 4, 5]
list2_to_zip = [1, '2', 4, 5]


def compare_zip(list1_to_zip: list, list2_to_zip: list) -> True or False:
    """
    Функция принимает на вход 2 списка и методом zip
    сравнивает их между собой, если один из елементов "?"
    он может считаться любым значением, если списки одинаковы
    на выходе True, если нет False
    """
    for i, j in zip(list1_to_zip, list2_to_zip):
        if i == j:
            continue
        elif (i == '?') or (j == '?'):
            continue
        else:
            return False
    return True


#  print(compare_zip(list1_to_zip,list2_to_zip))

# HW 17

list_to_filter = [2, 0, 5, 4, 2, 10]


#  print(numb.split(' '))
def filter_lef(list_to_filter: list) -> list or None:
    numb = input()
    sgf = numb.split(' ')
    if sgf[0] == 'Меньше':
        return list(filter(lambda x: x < int(sgf[1]), list_to_filter))
    elif sgf[0] == 'Больше':
        return list(filter(lambda x: x > int(sgf[1]), list_to_filter))
    else:
        print('Вы ввели не правильно')


#  print(filter_lef(list_to_filter))

# HW 18

# list_to_map = [2, 0, 4, 5, 1, 6, 9]


def map_work(list_to_map: list) -> list or None:
    multi = input()
    fgp = multi.split(' ')
    if fgp[0] == '*':
        return list(map(lambda x: x * int(fgp[1]), list_to_map))
    elif fgp[0] == '**':
        return list(map(lambda x: x ** int(fgp[1]), list_to_map))
    elif fgp[0] == '/':
        return list(map(lambda x: x / int(fgp[1]), list_to_map))
    elif fgp[0] == '+':
        return list(map(lambda x: x + int(fgp[1]), list_to_map))
    else:
        print('Вы ввели не правильно')


#  print(map_work(list_to_map, multi))

# HW 19

# def extra_map(list_to_map: list) -> list:
#     """
#     Функция принимает на вход список, далее принтует
#     вложенные функции и добавляет в список raduga
#     каждый элемент списка list_to_map деленный на numb
#     """
#     multi = input("Введите значения(прим:* 2):")
#     fgp = multi.split(' ')
#     multi = list(map(lambda x: x * int(fgp[1]), list_to_map))
#     stepen = list(map(lambda x: x ** int(fgp[1]), list_to_map))
#     delenie = list(map(lambda x: x / int(fgp[1]), list_to_map))
#     slozenie = list(map(lambda x: x + int(fgp[1]), list_to_map))
#     plt.plot(multi, label="Умножение", color='r', linestyle='-')
#     plt.plot(delenie, label="Деление", color='b', linestyle='--')
#     plt.plot(slozenie, label="Сложение", color='black', linestyle=':')
#     plt.plot(stepen, label="Степень", color='g', linestyle='-.')
#     plt.plot(list_to_map, label="Изначальный", color='brown')
#     plt.title('Графики списка')
#     plt.legend()
#     plt.show()
#     if fgp[0] == '*':
#         return multi
#     elif fgp[0] == '**':
#         return stepen
#     elif fgp[0] == '/':
#         return delenie
#     elif fgp[0] == '+':
#         return slozenie
#     else:
#         print('Вы ввели не правильно')


#  print(extra_map(list_to_map))

# HW 20

#  text = input()
#  type_to_text = str(input())

def lowup(text: str, type_to_text: str) -> list:
    if type_to_text == 'lower':
        #  print(text[0], 'Ento bukva')
        #  print(text[0].lower(), 'a ento malenkaya bukva')
        #  print(text.lower(), 'a ento vsya stroka')
        lower_text = list(filter(lambda x: x == x.lower(), text))
        return ''.join(lower_text)
    elif type_to_text == 'upper':
        upper_text = list(filter(lambda x: x == x.upper(), text))
        return ''.join(upper_text)


#  print(lowup(text, type_to_text))

# HW 21

list_to_minus = [4, 6, 2, 2, 4]
znach = 3


def func_minus_list(list_to_minus: list, znach: int) -> list:
    ipf = 0
    eoa_list = []
    while (list_to_minus[ipf] - znach) >= 0:
        eoa_list.append(list_to_minus[ipf] - znach)
        ipf += 1
    return eoa_list


#  print(func_minus_list(list_to_minus,znach))

# HW 22

words_in_time = "Я ЛЮБЛЮ ПРОГАТЬ БОЛЬШЕ ЧЕМ ИГРАТЬ, И ОБЕЩАЮ ПРОГАТЬ ЛУЧШЕ И БОЛЬШЕ!"


def time_check(words_in_time: str) -> str or None:
    """
    Функция с течением указанного времени в секундах, будет печатать строку
    каждую секунду и печатать время до её окончания.
    """
    sec = int(input())
    while sec > 0:
        print(words_in_time, "Осталось", sec, "секунды.")
        sec -= 1
        time.sleep(1)


#  print(time_check(words_in_time))

# HW 23

def square() -> None:
    """
    Функция принтует прямоугольник указанных размеров.
    """
    num = input()
    two_nums = num.split(',')
    if len(num) < 2:
        print(' ', '-' * int(num))
        for i in range(int(num)):
            print('|', ' ' * int(num), '|')
        print(' ', '-' * int(num))
    else:
        print(' ', '-' * int(two_nums[1]))
        for i in range(int(two_nums[0])):
            print('|', ' ' * int(two_nums[1]), '|')
        print(' ', '-' * int(two_nums[1]))


#  print(square())

# HW 24

list_to_sum = [0, -1, 7, 2, 5]
#  sign = input()
list_to_sum2 = []


def sum_numb(list_to_sum: list, sign: str, list_to_sum2: list) -> int or float:
    """
    Функция в зависимости от введенного знака
    будет считать положительные или отрицательные значения списка
    """
    if sign == '+':
        if len(list_to_sum) == 0:
            return sum(list_to_sum2)
        elif list_to_sum[0] < 0:
            list_to_sum.pop(0)
            return sum_numb(list_to_sum, sign, list_to_sum2)
        else:
            list_to_sum2.append(list_to_sum[0])
            list_to_sum.pop(0)
            return sum_numb(list_to_sum, sign, list_to_sum2)
    if sign == '-':
        if len(list_to_sum) == 0:
            return sum(list_to_sum2)
        elif list_to_sum[0] > 0:
            list_to_sum.pop(0)
            return sum_numb(list_to_sum, sign, list_to_sum2)
        else:
            list_to_sum2.append(list_to_sum[0])
            list_to_sum.pop(0)
            return sum_numb(list_to_sum, sign, list_to_sum2)


#  print(sum_numb(list_to_sum, sign, list_to_sum2))


#  #  def sum_num2(list_to_sum, sign):
#  if sign == '+':
#      beg = list(map(lambda x: x if x > 0 else 0, list_to_sum))
#  else:
#      cef = list(map(lambda x: x if x < 0 else 0, list_to_sum))
#  print(sum(beg))
#  get = [i for i in range(10)]
#  def my_generator(x:int):
#      for i in range(x):
#          yield i
#
#  get = (i for i in range(10))
#  print(list(get))

# HW 25

# def validation_json() -> list:
#     with open("files/usersID.json") as uID:
#         data = json.load(uID)
#         print(data)
#         while True:
#             login = input("Введите логин: ")
#             if login in data.keys():
#                 password = input("Введите пароль: ")
#                 if (login, password) in data.items():
#                     return extra_map(list_to_map)
#                     break
#                 else:
#                     print("Ввели не правильный логин или пароль")
#                     continue
#             else:
#                 print("Ввели не правильный логин")
#                 continue


# print(validation_json())
# Создать форму регистрации, функцию которая будет логин пароль админа, а после верификации создавать логин парлль обычных юзеров и всё это сохранить в json

# HW 26

# сайт цбр, реализовать к этому ресурсу доступ по api, получить с него курс валют и выводить в рублях
#  data2 = {"put something":"somethings"}
#  local_serv = requests.put("https://reqres.in/api/users?page=2", json=data2)
#
#  print(local_serv.text)

#
#  Добавить json с хешами для сохранности
#  with open("files/usersID.json") as uID:
#      data = json.load(uID)
#      print(data)
#  print(hashlib.md5(str(data).encode("utf-8")).hexdigest())

#
#  отобразить сколько в общем семья платит за каждый продукт
randlist = (1, 2, 4)


#  print(hash(randlist))

# HW 27

def score_stroke() -> str:
    """
    Функция считает колличество повторяющихся букв в переменной
    my_str и выводит строку с буквой и колличеством её повторений.
    """
    my_str = input()
    score = 1
    answ = ""
    for i in range(len(my_str) - 1):
        if my_str[i] == my_str[i + 1]:
            score += 1
        else:
            answ = answ + my_str[i] + str(score)
            score = 1
    answ = answ + my_str[-1] + str(score)
    return answ


#  print(score_stroke())

# HW28

val = 7


def bank_exchange(val: int) -> str or int:
    bank = [100, 5]

    try:
        exch_to_one = (val % bank[1]) // bank[2]
        exch_to_ten = val // bank[0]
        exch_to_five = (val % bank[0]) // bank[1]
    except IndexError:
        return print("net razmena")
    return print(exch_to_ten, exch_to_five, exch_to_one)


# bank_exchange(val)

# HW 29

# def validation_json() -> dict:
#     """
#     Функция проводит валидацию логина пароля админа
#     и после правлиьного ввода позволяет добавить
#     новых пользователей и добавляет в их хеш файл hash.json.
#     """
#
#     with open("files/test2.json") as tst:
#         data = json.load(tst)
#         print(data)
#         login = input()
#         if login in data.keys():
#             password = input()
#             if password == data[login]:
#                 users = json.load(open("files/usersID.json"))
#                 with open("files/usersID.json", "w") as uID:
#                     for i in range(1):
#                         i = input()
#                         users[i] = input()
#                     json.dump(users, uID)
#     hashus = {"users": hashlib.md5(str(users).encode("utf-8")).hexdigest()}
#     with open("files/hash.json", "w") as hsh:
#         json.dump(hashus, hsh)
#     return users


# print(validation_json())

# HW 30

def crb_valute() -> None:
    """
    Функция выводит курс валют
    с сайта ЦРБ за вчера и сегодня.
    """
    valute_name = str(input())
    valute_name = valute_name.upper()
    local_serv = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    val_dict = dict(local_serv.json())
    if valute_name in val_dict['Valute']:
        print("Вчера один", (val_dict['Valute'][valute_name]['Name']), "был равен",
              (val_dict['Valute'][valute_name]['Value']), "руб.")
        print("Сегодня один", (val_dict['Valute'][valute_name]['Name']), "равен",
              (val_dict['Valute'][valute_name]['Previous']), "руб.")
    else:
        print("Указанная валюта не найдена")


# crb_valute()

# пощупать пандас влхимию сделать insert join delete
# перенести HW 29 в бд последством алхимии
# объеденить дз по валидации в один класс и сделать __защищенной функции коннекта к бд

# HW 31

class MyRaduga:

    def __init__(self, value: list):
        self.value = value

    def extra_map(self, value: list) -> list:
        """
        Функция принимает на вход список, далее принтует
        вложенные функции и добавляет в список raduga
        каждый элемент списка list_to_map деленный на numb
        """
        multi = input("Введите значения(прим:* 2):")
        fgp = multi.split(' ')
        multi = list(map(lambda x: x * int(fgp[1]), value))
        stepen = list(map(lambda x: x ** int(fgp[1]), value))
        delenie = list(map(lambda x: x / int(fgp[1]), value))
        slozenie = list(map(lambda x: x + int(fgp[1]), value))
        plt.plot(multi, label="Умножение", color='r', linestyle='-')
        plt.plot(delenie, label="Деление", color='b', linestyle='--')
        plt.plot(slozenie, label="Сложение", color='black', linestyle=':')
        plt.plot(stepen, label="Степень", color='g', linestyle='-.')
        plt.plot(value, label="Изначальный", color='brown')
        plt.title('Графики списка')
        plt.legend()
        plt.show()
        if fgp[0] == '*':
            return multi
        elif fgp[0] == '**':
            return stepen
        elif fgp[0] == '/':
            return delenie
        elif fgp[0] == '+':
            return slozenie
        else:
            print('Вы ввели не правильно')


class MyValidationPostgres(MyRaduga):
    """
    Класс MyValidationPostgres является дочерним класса MyRaduga
    и создает движок бд postgres а далее
    на основе данных с бд проверяет валидацию юзеров,
    после успешного прохождения валидации вызывает метод родительского класса extra_map.
    """
    __engine = sqal.create_engine("postgresql://gin:1337@localhost:8000/log_user", echo=False)
    __meta = sqal.MetaData(bind=__engine, schema='users')
    __user = sqal.Table('users', __meta, autoload=True)

    __s = __user.select()
    __r = __engine.execute(__s)
    __t = __r.fetchall()
    __user_type = input('Введите логин: ')

    __z = list(i[1] for i in __t)
    __p = list(i[2] for i in __t)

    def my_raduga(self) -> None:
        match self.__z:
            case [*args] if self.__user_type == 'root' and self.__user_type in self.__z:
                if input('Введите пароль: ') in self.__p:
                    ins = self.__user.insert().values(
                        id_user=input('id_user: '),
                        user_name=input('user_name: '),
                        user_password=input('user_password: '),
                        user_role=input('user_role: '),
                        user_mailadress=input('user_mailadress: '),
                        user_status=1
                    )
                    self.__engine.execute(ins)
            case [*args] if self.__user_type in self.__z:
                pas = input('Введите пароль: ')
                if pas in self.__p:
                    MyRaduga.extra_map(self, self.value)
            case _:
                print('Неверный логин или пароль.')

    __hashus = {"users": hashlib.md5(str(__t).encode("utf-8")).hexdigest()}
    with open("files/hash.json", "w") as hsh:
        json.dump(__hashus, hsh)


b = MyValidationPostgres(list_to_sum)
b.my_raduga()


# HW 32

class MyValidation:

    def __validation_json(self) -> dict:
        """
        Функция проводит валидацию логина пароля админа
        и после правлиьного ввода позволяет добавить
        новых пользователей и добавляет в их хеш файл hash.json.
        """
        with open("files/test2.json") as tst:
            data = json.load(tst)
            print(data)
            login = input()
            if login in data.keys():
                password = input()
                if password == data[login]:
                    users = json.load(open("files/usersID.json"))
                    with open("files/usersID.json", "w") as uID:
                        for i in range(1):
                            i = input()
                            users[i] = input()
                        json.dump(users, uID)
        hashus = {"users": hashlib.md5(str(users).encode("utf-8")).hexdigest()}
        with open("files/hash.json", "w") as hsh:
            json.dump(hashus, hsh)
        return users


list_to_map = [2, 0, 4, 5, 1, 6, 9]

# a = MyRaduga(MyValidation)
# a.extra_map(list_to_map)
