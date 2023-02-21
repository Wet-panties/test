def decorator(count):
    def dec(function):
        import time

        def wrapper(*args, **kwargs):
            print(f'Starting {function}')
            start = time.time()
            for a in range(count):
                result = function(*args, **kwargs)
                if a + 1 == 2:
                    raz = 'раза'
                elif (a + 1) == 3:
                    raz = 'раза'
                elif (a + 1) == 4:
                    raz = 'раза'
                else:
                    raz = 'раз'
                print(f' {result} {a + 1} {raz}')
            fin = time.time() - start + 0.003
            print(f'{function} successfully ended in {fin}')
            return result

        return wrapper

    return dec


@decorator(count=10)
def helloeblo(name):
    helloname = f'{name} мы тут выебали твою мать'
    return helloname


urname = input('Тварина, как тебя зовут?:  ')
print(helloeblo(urname))

'''def hellodeco():
    def helloeblo():
        print('привет сын шлюхи')

    helloeblo()


def newfuck(func):
    print(f'Получена функция {func} Запускаю')
    func()
    print(f'{func} gotova!')


hellodeco()
newfuck(hellodeco)'''
