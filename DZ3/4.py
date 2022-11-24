numbers = [2,2,3,3,4,3,3,6,23,2,453,213,122,44,11235,788,9900,9900,9900,9900,9900,1,1,1,1]
list_count=[0] # список для записи частоты каждого элемента.1-й элемент 0 ,чтобы не вводить try-except при 1й итерации и [-2]
for num in set(numbers):
    list_count.append(numbers.count(num))
    if list_count[-1]>=max(list_count):
        frequent_num = num

print (f'самое частое число в списке {frequent_num}')