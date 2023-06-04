import random

n1 = int(input("Введите количество 1 последовательности чисел n1 "))
n2 = int(input("Введите количество 2 последовательности чисел n2 "))

lst1 = list()
lst2 = list()
lst3 = list()

k=0;

for i in range(n1):
    k = random.randint(-5,5)
    lst1.append(k) 
print(lst1)
lst1 = set(lst1) 
print(lst1)
for i in range(n2):
    k = random.randint(-5,5)
    lst2.append(k) 
print(lst2)
lst2 = set(lst2)
print(lst2)

k=0
for i in lst1:
    for j in lst2:
        if i == j:
            lst3.append(i)
            k += 1
print()                   
print(sorted(lst3))

