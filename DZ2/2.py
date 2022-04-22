import sys
n = [i if i.isdigit() else sys.exit('Ввели не число') for i in input('Введите число:  ')]
x=0 # счетчик четных
y=0 # счетчик нечетных


for i in n:
    if (int(i)%2) == 0 :
        x=x+1
    else: y=y+1
print (f'В введенном числе {x} четных и {y} нечетных чисел')
