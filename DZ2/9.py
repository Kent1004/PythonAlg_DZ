import sys
numbers = [i if i.isdigit() else sys.exit('Ввели не число') for i in input('Введите последовательность чисел через пробел: ').split()]
sum_list = []

for number in numbers:
    sum_number=0
    for num in number:
        sum_number=sum_number + int(num)
    sum_list.append(sum_number)
print (f'Максимальная сумма цифр {max (sum_list)} у введенного числа {numbers[sum_list.index(max (sum_list))]}')







