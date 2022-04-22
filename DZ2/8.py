import sys
numbers = [i if i.isdigit() else sys.exit('Ввели не число') for i in input('Введите последовательность чисел через пробел: ').split()]
digit = input ('Введите цифру: ')
count = 0
for number in numbers:
    for num in number:
        if num == digit: count = count +1

print(f'Цифра {digit} встречается {count} раз')