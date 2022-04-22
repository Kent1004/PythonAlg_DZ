numbers = [2,-3,3,-4,3,3,6,-23,-2,-453,213,-122,-44,11235,788,9900,1]
neg_num=[num for num in numbers if num < 0 ]
print (f'макс. отриц. эл-т {max(neg_num)} на позиции {numbers.index(max(neg_num))}')

