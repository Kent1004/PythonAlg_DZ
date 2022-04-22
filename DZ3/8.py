j = 0
matrix=[]
while j <4:
    numbers = [int(i) if i.isdigit() else sys.exit('Ввели не число') for i in input('Введите 4 числа: ').split()]
    if len(numbers)!=4 : print('Вы ввели не 4 числа')
    while len(numbers) != 4:
        numbers = [int(i) if i.isdigit() else sys.exit('Ввели не число') for i in input('Введите 4 числа: ').split()]
        if len(numbers) != 4: print('Вы ввели не 4 числа')
    numbers.append(sum(numbers))
    matrix.append(numbers)
    j+=1
for lists in matrix: print(*lists)
