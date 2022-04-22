numbers = [2,-3,3,-4,3,3,6,-23,-2,-453,213,-122,-44,11235,788,333,477,9900,1]
if numbers.count(min(numbers)) > 1 : print (f'минимальные числа массива {min(numbers)} и {min(numbers)}')
else:
    min1 = min(numbers)
    numbers.remove(min1)
    print(f'минимальные числа массива {min1} и {min(numbers)}')
