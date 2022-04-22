j = 0
# matrix = [ [12, 22, 44, 55, 133],[0,45,66,33,156],[9,55,66,99,232],[29,33,44,33,132]]
# matrix = [[1,266,355,4,10],[55,33,11,66,165],[123,546,67,3324,4060],[22,88,33,66,209]]
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


column_min= []
lists_min=[]
for i in range(0,5):
    for j in  range(0,4):
        column_min.append(matrix[j][i])
    lists_min.append(min(column_min))
    column_min.clear()

print('Максимальный элемент среди минимальных элементов столбцов матрицы равен: ', max(lists_min))

