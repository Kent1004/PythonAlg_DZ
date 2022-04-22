# numbers = [int(i) if i.isdigit() else sys.exit('Ввели не число') for i in input('Введите последовательность чисел через пробел: ').split()]
numbers = [2,3,3,4,3,3,6,23,453,213,122,44,11235,788,9900]

pos_min = numbers.index(min(numbers))
pos_max= numbers.index(max(numbers))
a= numbers[pos_min]
b = numbers[pos_max]
numbers[pos_min] = b
numbers[pos_max]=a

print(numbers)