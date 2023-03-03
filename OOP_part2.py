class House:
    FOUNDATION = 'strip'  # константа

    roof = 'шифер'

    def __init__(self,
                 floor: int):
        """конструктор дома: площадь, этажи, материал стен. конструктор всегда запускается с __init__(self)вместо
        self может быть любое слово """
        # присваиваем параметры конструктора к переменной
        self.__sq = 15
        self._fl = floor  # защищенная переменная
        self.__w = 'Brick'  # приватная переменная
        print('дом построен')

    @property
    def square(self):
        return self.__sq

    @square.setter
    def square(self,
               set_square: int):
        if type(set_square) == int:
            if set_square < 15:
                self.__sq = 15
            elif set_square > 100:
                self.__sq = 100
            else:
                self.__sq = set_square
        else: print('error, square должен быть int')

    @property  # декоратор-обёртка для упрощения вывода без вызова доп функции
    def wall(self):
        return self.__w

    @wall.setter  # декоратор для упрощенного придания значения переменной
    def wall(self, wall):
        self.__w = wall

    def build_balcony(self, i):
        """вычитание первого значения из конструктора """
        self.__sq -= i

    def build_roof(self):
        """уебали крышу"""
        print('уебали крышу материалом ' + self.roof)


houseP = House(5)
houseP.wall = 'Beton'

print(houseP._House__sq)


# houseP.square = 'zalupa'
# print(houseP.square)

# houseP = House(100, 5, 'Кирпич ёбаный')
# print(houseP._House__w) # обращение к приватным свойствам класса houseP.w превратилось в houseP._House__w
# houseP._House__w = 'Test'
# print(houseP._House__w)


# houseP.FOUNDATION = 'NOT strip'
# print(houseP.FOUNDATION)
# print(houseP.roof)
# houseP.roof = 'Test'
# print(houseP.roof)
#                         # разные аттрибуты
# print(House.roof)


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
