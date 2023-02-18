#
#
#  Вложенные переменные не влияют на глобальную, пока не применишь из функции global


variable = 'Global'
def test():
    #global variable
    variable = 'local'
    print(variable)


    def test_two():
        #global variable
        variable = 'Local two'
        print(variable)
    test_two()


test()

print(variable)









'''def SumSQ(a, b, c=2):
    z = (a + b)**c
    return z


def args(*args):
    for a in args:
        print(a)


#args(1, 2, 3, 3, 3, 3, 42424, 'pedik', 3, 3, 3, 3, 3, 3, 3, False, True, None)


def kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k)
        print(v)


kwargs(Alex=35, Boris=26)


result = SumSQ(3, 5)
print(result)'''
