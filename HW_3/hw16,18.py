import random
n = int(input("Введите количество элементов списка "))
x = int(input("Введите любое число "))
lst1 = list()
lst2 = list()
for i in range(n): 
    #k = int(input("Введите элементы списка "))
    k = random.randint(0,5)
    lst1.append(k)
    lst2.append(abs(k-x))
print(lst1)
print(lst2)
min = lst2[0]
i = 0
while (i < n):
    if lst2[i] != 0:
        min1 = lst2[i]
        break
    i += 1
count = 0
p = 0
i = 0
p1 = 0
while (i < n):
    if x == lst1[i]:
        count +=1
    if lst2[i] < min:
        min = lst2[i]
        p = i
    if (lst2[i] != 0):
        if (lst2[i] < min1):
            min1 = lst2[i]
            p1 = i
    i += 1 
if (count > 0):
    print(f"\n Число {x} встречается в списке {lst1} --> {count} раз(а)")
else:
    print(f"\n Число {x} отсутствует в списке {lst1}")
if min == 0:
    print(f"\n Самое первое близкое число к {x} в списке {lst1} - это {lst1[p1]}")
else:
    print(f"\n Самое первое близкое число к {x} в списке {lst1} - это {lst1[p]}")