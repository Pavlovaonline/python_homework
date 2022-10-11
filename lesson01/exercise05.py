
from random import randint, random
from xml.dom import xmlbuilder

x= int(input("Введите количество строк: "))
y= int(input("Введите количество столбцов: "))
mas = [[randint(1, 100) for j in range(y)] for i in range(x)]
print("Массив {}x{}: \n".format(x,y), mas)

newMas = []
for i in mas:
    for j in i:
        newMas.append(j)
mas = sorted(newMas)

print("Упорядоченный массив: ")
for i in range(0, len(mas), x):
    newMas = mas[i : x + i]
    if len(newMas) < x:
        newMas += [None for j in range(y - len(newMas))]
    print(list(newMas))

