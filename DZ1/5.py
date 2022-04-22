import sys
x,y = [i.lower() for i in input('Введите буквы латинского алфавита:  ').split()]
'''Проверка корректности  введеных данных'''


if not x.isalpha() or not y.isalpha() :
    print("Вы ввели некорректный диапазон")
    sys.exit()
elif x == y:
    print("Вы ввели некорректный диапазон")
    sys.exit()
else:
    print (f'Вы ввели {ord(x) - 96} и {ord(y) - 96} буквы латинского алфавита, между ними букв: {(abs(ord(x) - ord(y)) - 1)}')
