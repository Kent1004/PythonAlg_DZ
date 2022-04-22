import sys
def mirror(n):
    if len(n)==1:return (n[-1])
    else : return n[-1]+mirror(n[:-1])

print(mirror([i if i.isdigit() else sys.exit('Ввели не число') for i in input('Введите число:  ')]))
