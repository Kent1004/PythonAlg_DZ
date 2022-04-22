n = int(input('Введите любое натуральное  число '))

summa1=0

for i in range(1,n+1):
    summa1 = summa1+i

if summa1 == n*(n+1)/2: print ('Равентсво выполняется')
else: print ('Равентсво не выполняется')