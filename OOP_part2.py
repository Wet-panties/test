class SuperHouse:


    roof = 'шифер'

    def __init__(self,
                 square: int,
                 floor: int,
                 wall: str):
        '''конструктор дома: площадь, этажи, материал стен. конструктор всегда запускается с __init__(self)вместо self может быть любое слово'''
        # присваиваем параметры конструктора к переменной
        self.sq = square
        self.fl = floor
        self.w = wall
        print('дом построен')

    def build_balcony(self, i):
        '''вычитание первого значения из конструктора '''
        self.sq -= i

    def build_roof(self):
        '''уебали крышу'''
        print('уебали крышу материалом ' + self.roof)


class House
















# вывод переменной из класса, но нельзя вывести из конструктора до объявления houseP
print(House.roof)
# print(House.sq) # выдаст ошибку

houseP = House(100, 5, 'Кирпич ёбаный')
print(houseP.roof)
houseP.roof = 'Test'
print(houseP.roof)
                        # разные аттрибуты
print(House.roof)

# # указываем обязательные параметры, которые передаём в конструктор и сокращаем вызов функций
# # из класса House в переменную houseP и обращаемся к классу только через неё
# House.roof = 'залупа'
# houseP = House(100, 5, 'Гиспокартон')
# # print(houseP.sq) не выдаст ошибку
# print(houseP.sq)
# print(houseP.roof)







# # выводим значение self.sq из класса
# print(f'площадь дома {houseP.sq}')
#
# # передаём переменную i
# houseP.build_balcony(10)
#
# # повторно выводим значение self.sq из класса
# print(f'площадь дома после запуска метода {houseP.sq}')
# houseP.build_roof()
#
# print(type(houseP))
#
#
# # MyHome
