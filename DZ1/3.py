import sys
x1,y1 = [int(i)  for i in input('Введите координаты 1й точки ').split()]
x2,y2 = [int(i)  for i in input('Введите координаты 2й точки ').split()]
print ('Заданы точки М1({},{})  и M2({},{})'.format(x1,y1,x2,y2))
if x1 == x2 : print (f'Прямая паралельна оси Oy, уравнение прямой : x= {x1}')
elif y1==y2 : print (f'Прямая паралельна оси Ox, уравнение прямой : y= {y1}')
else: print ('Уравнение прямой: y = {}*x+{}'.format(((y2-y1)/(x2-x1)),(y1 - ((y2-y1)/(x2-x1))*x1)))


