import random

x= random.randint(0,100)
print(x)
i = 1
while (y:=int(input('Введите число '))) :
    if i == 10:
        print ('Вы не угадали, загаданное число: ',x)
        break
    elif y>x : print('Введенное число больше загаданного ')
    elif y<x: print('Введенное число меньше загаданного ')
    elif y==x:
        print('Вы угадали: ',y)
        break
    i=i+1
