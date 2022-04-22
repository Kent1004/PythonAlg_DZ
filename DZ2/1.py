import sys

actions=  '0+-*/'
ch=''

while True:
    while actions.find(ch:=input('Введите +-*/ или 0 для завершения: '))<0: pass
    if ch=='0': sys.exit('Программа завершена')
    else:
        x, y = [i if i.isdigit() else sys.exit('Ввели не число') for i in input('Введите 2 числа:  ').split()]
        if ch == '/' and  y =='0': print('Деление на ноль не возможно')
        else: print(eval(x + ch + y))



