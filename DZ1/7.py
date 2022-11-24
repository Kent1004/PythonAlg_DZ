import sys
x,y,z = [int(i) if i.isdigit() else sys.exit('Отрезок не верный') for i in input('Введите длину трех отрезков:  ').split() ]


if x+y<z or y+z<x or x+z<y:
    print ("Треугольник не может сущестовать из указанных отрезков")
    sys.exit()
elif x ==  y  == z : print("Треугольник равносторонний")
elif x==y or x==z or z==y : print("Треугольник равнобедренный")
else: print("Треугольник разносторонний")



