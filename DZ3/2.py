numbers = [int(i) if i.isdigit() else sys.exit('Ввели не число') for i in input('Введите последовательность чисел через пробел: ').split()]
# numbers = [2,3,3,2,3,3,2]
indexes  = [ i for i in range(len(numbers)) if numbers[i]%2 == 0 ]

print(indexes)