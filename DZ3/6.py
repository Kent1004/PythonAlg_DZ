numbers = [2,-3,3,-4,3,3,6,-23,-2,-453,213,-122,-44,11235,788,333,477,9900,1]
if numbers.index(min(numbers))< numbers.index(max(numbers)):
    print('Сумма элементов между мин и макс равна: ',sum(numbers[(numbers.index(min(numbers))+1):numbers.index(max(numbers))]))
else:print('Сумма элементов между мин и макс равна: ',sum(numbers[(numbers.index(max(numbers))+1):numbers.index(min(numbers))]))
