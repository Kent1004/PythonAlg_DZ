import datetime
import sys
x = input('Введите год:  ')
'''Проверка корректности  введеных данных'''
if not x.isdigit() or len(x)>4:
    print("Вы ввели некорректный год")
    sys.exit()
try:
    if datetime.date(int(x),2,29): print ('Год високосный')
except ValueError:
    print ('Год не високосный')