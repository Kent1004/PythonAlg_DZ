a = 5
b = 6
d =~ a
c=~b
print (f' a = 5 , b = 6')
print (f'a & b : {bin(a)} & {bin(b)}  = {bin(a&b)}')
print (f'a | b : {bin(a)} | {bin(b)}  = {bin(a|b)}')
print (f'a ^ b : {bin(a)} ^ {bin(b)}  = {bin(a^b)}')
print ('d =~ a  : d =~ {} , d = {} ,  {}'.format(a,bin(d),d))
print ('c =~ b  : c =~ {} , c = {} ,  {}'.format(b,bin(c),c))
print ('a<<2 ,a в 2-й СИ {} : 1-й сдвиг {} ; 2-й сдвиг {}- результат в 10-й СИ {}'.format(bin(a),bin(a<<1),bin(a<<2),a<<2))
print ('a>>2 ,a в 2-й СИ {} : 1-й сдвиг {} ; 2-й сдвиг {}- результат в 10-й СИ {}'.format(bin(a),bin(a>>1),bin(a>>2),a>>2))


