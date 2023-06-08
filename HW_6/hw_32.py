# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

import random

lst = [random.randint(-10, 10) for _ in range(10)]
print(lst)

min = int(input("Введите min число "))
max = int(input("Введите max число "))
i = 0 
for i in range(len(lst)):
    if min<= lst[i]<= max:             
        print(i, end=" ")
print()