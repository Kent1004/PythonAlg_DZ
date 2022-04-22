import sys
x,y,z = [int(i) if i.isdigit() else sys.exit('Ввели не числа') for i in input('Введите три числа:  ').split() ]
if (x<y and x>z) or (x>y and x<z): print (f'{x} среднее число')
elif (y<x and y>z) or (y>x and y<z): print (f'{y} среднее число')
elif (z<x and z>y) or (z>x and z<y): print (f'{z} среднее число')
else : print ('Введены равные числа')

