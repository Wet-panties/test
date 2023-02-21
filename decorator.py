def decorator(count):
    def dec(function):
        import time
        def wrapper(*args, **kwargs):
            print(f'Starting {function}')
            start = time.time()
            for a in range(count):
                result = function(*args, **kwargs)
                print(f'Blowing {count} times - {result} #{a+1}')
            fin = time.time() - start + 0.003
            print(f'{function} successfully ended in {fin}')
            return result
        return wrapper
    return dec


@decorator(count=5)
def helloeblo(name):
    helloname = f'hello {name}'
    return helloname


test = helloeblo('EBLO')
print(test)













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
