import time
import sys
import string as st

'''функция проверки вещественного числа'''
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

num_float = 0 # тригер вещественного числа
in_alpha = 0
rand =0
x1=0 # для диапазона дробной части вещественного числа
y1=1  #для диапазона дробной части вещественного числа
dec_part =0 # дробная чачть вещественного числа по умолчанию
x,y = [i for i in input('Введите диапозон для генерации случайного целого или вещественного числа через пробел:  ').split()]
'''Проверка корректности  введеных данных'''

if x.isalpha() and y.isalpha() and ord(x) < ord(y):
    y = str(ord(y) - ord(x))
    x_alpha = ord(x)
    x='0'
    in_alpha = 1
# elif not (x.isalpha() and y.isalpha()):
#     print("Вы ввели некорректный диапазон1")
#     sys.exit()
elif not  (x[0]=='-' and  x[1:].isdigit() or x.isdigit() or isfloat(x)):
    print("Вы ввели некорректный диапазон2")
    sys.exit()
elif not(y[0]=='-' and  y[1:].isdigit() or  y.isdigit() or isfloat(y)):
    print("Вы ввели некорректный диапазон3")
    sys.exit()
elif  float(x)>float(y) :
    print("Вы ввели некорректный диапазон4")
    sys.exit()
elif x.isalpha() and y.isalpha()  and ord(x) >= ord(y):
    print("Вы ввели некорректный диапазон5")
    sys.exit()


'''если число вещественное , разбиваем его на целую часть и дробную'''
if float(x)%1 !=0  or float(y)%1 !=0 :
    x1 = float(x)%1
    y1=float(y)%1
    x =x.split('.')[0]
    y=y.split('.')[0]
    num_float=1
'''Вдиапозон букв'''

minus = 0
y_buf = y
x_buf = x
'''целые части чисел диапозона приводим к необходимому диапозону в зависимоти от условий'''
if x[:1]=='-' and y[:1]=='-':
    y_buf  = y[1:]
    y=x[1:]
    x=y_buf
if x[:1]=='-' and y[:1].isdigit():
    if abs(int(x)) == abs(int(y)):  x='0'
    else:
        z = abs(int(x)) + abs(int(y))
        y = str(z)
        x = '1'
'''метод не может обработать число кратное 10 , поэтому вычитаем 1 или прибавляем'''
if int(x)!=0 and int(x)%10==0 : x=str(int(x)+1)
if int(y)!=0 and int(y)%10 == 0: y=str(int(y)-1)



i=-1 # -1 , чтобы для разрядности i могла выпасть случайным образом 0
'''генерируем случайнуй разрядность генерируемого числа в случае чисел с разными разрядами'''
rand = time.time()
while len(y)!=1 and (i==-1 or i>len(y)) :
    rand = time.time()
    i=int(str(rand)[-2:-1])
if len(x) == len(y) : i = 0
'''генерируем случайное число через модуль time.time , состоящее из послдених цифр текущего времени'''
if int(x)==0 and int(y)==0: rand =0
# elif int(str(rand)[-(i+len(x)):])>int(x) and int(str(rand)[-(i+len(x)):])<int(y): print (i,'dasdasdasdas')
else:
    '''используем исключение , тк time.time может вернуть до запятой меньшее число, чем требуется в заданном диапозоне'''
    while True:
        try:
            while (int(str(rand)[-(i+len(x)):])<int(x) or int(str(rand)[-(i+len(x)):])>int(y))  :
                rand = time.time()
                # print(rand)
            break
        except ValueError:
            pass
'''генерируем случайную дробную часть в рамках заданного диапозона'''
if x1 == y1 and num_float == 1:
    dec_part = x1
elif num_float == 1 and x1<y1:
    rand1 = time.time()
    while (rand1 % 1 < x1 or rand1% 1 > y1):
        rand1 = time.time()
    dec_part = rand1 % 1
elif num_float == 1 and x1>y1:
    rand1 = time.time()
    while rand1 % 1 < x1 and rand1% 1 > y1:
        rand1 = time.time()
    dec_part = rand1 % 1


'''в зависимости от значения x   и  y выводим случайное число
r - сгенерированное число
|x|>|y| и r>|x| -> r - x
|x|>|y| и r<|x|-> -r
|x|<|y| и r>|y| -> r - y
|x|<|y| и r<|y|-> r
|x|=|y|  и r[-1:] - четное -> r
|x|=|y|  и r[-1:] - нечетное -> -r
'''

if int(str(rand)[-(i+len(x)):]) > abs(int(x_buf)) and abs(int(x_buf))>abs(int(y_buf)) : print('Случайоное число: ',int(str(rand)[-(i+len(x)):]) - abs(int(x_buf))+dec_part)
elif int(str(rand)[-(i+len(x)):]) < abs(int(x_buf)) and abs(int(x_buf))>abs(int(y_buf)): print(f'Случайоное число: -{int(str(rand)[-(i + len(x)):])+dec_part}')
elif int(str(rand)[-(i+len(x)):]) > abs(int(y_buf)) and abs(int(x_buf))<abs(int(y_buf)): print(f'Случайоное число: -{int(str(rand)[-(i+len(x)):]) - abs(int(y_buf))++dec_part}')
elif int(str(rand)[-(i+len(x)):]) < abs(int(y_buf)) and abs(int(x_buf))<abs(int(y_buf)):
    if in_alpha==1:  print('Случайный символ:',chr(int(str(rand)[-(i+len(x)):])+dec_part+x_alpha))
    else: print('Случайоное число:',int(str(rand)[-(i+len(x)):])+dec_part)
elif int(str(rand)[-1:])%2 == 0: print('Случайоное число:',int(str(rand)[-(i+len(x)):])++dec_part)
else: print(f'Случайоное число: -{int(str(rand)[-(i + len(x)):])+dec_part}')



