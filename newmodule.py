'''
Строк документации.
Для примера работы с модулями и вариантов импорта
'''


def newf(par):
    '''
    Функция возвращает число в квадрате.
    Принимает 1 аргумент int или float.
    '''
    return par**2

'''В модуле могут быть и переменные'''

k = 7
k2 = ['Список', 'из', 'строк']

if __name__== '__main__':
    print(newf(float(input('Введите число'))))