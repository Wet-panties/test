class House:

    def __init__(self,
                 square: int,
                 floor: int,
                 wall: str):
        '''конструктор дома: площадь, этажи, материал стен. конструктор всегда запускается с __init__(self)вместо self может быть любое слово'''
        # присваиваем параметры конструктора к переменной
        self.sq = square
        self.fl = floor
        self.w = wall
        print('залупа построена')

    def build_balcony(self, i):
        '''вычитание первого значения из конструктора '''
        self.sq -= i

    def build_roof(self):
    '''уебали крышу  '''


# указываем обязательные параметры, которые передаём в конструктор и сокращаем вызов функций из класса House в переменную houseP
houseP = House(100, 5, 'Гиспокартон')

# выводим значение self.sq из класса
print(f'площадь дома {houseP.sq}')

# передаём переменную i
houseP.build_balcony(10)

# повторно выводим значение self.sq из класса
print(f'площадь дома после запуска метода {houseP.sq}')
print(type(houseP))

# MyHome
