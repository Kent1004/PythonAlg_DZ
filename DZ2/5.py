i = 32
result = ''
while (i)>=32 and (i<=127):
    if ((i-32)%10) == 0: result=result+'\n' + f'{i}-{chr(i)} '
    else: result=result+ f'{i}-{chr(i)} '
    i=i+1
print(result)
