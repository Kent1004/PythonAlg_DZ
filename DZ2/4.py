def summa(n,i = -2):
    if n==1:
        return i*(-0.5)
    else:
        return i*(-0.5) + summa(n-1,i*(-0.5))


print(summa(int(input('Введите длинну последовательности:  '))))
