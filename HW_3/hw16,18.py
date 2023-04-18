import random
n = int(input("Введите количество элементов списка "))
x = int(input("Введите любое число "))
list_1 = list()
for i in range(n): 
    #k = int(input("Введите элементы списка "))
    k = random.randint(0,5)
    list_1.append(k)
print(list_1)
count = 0
i = 0
while (i < len(list_1)):
    if x == list_1[i]:
        count +=1        
    i += 1
if (count > 0):
    print(f"\n Число {x} встречается в списке {count} раз(а)")
min = 0;
p = 0;
i = 0
if count == 0:
    while (i < len(list_1)):
        if abs(x - list_1[0]) > abs(x - list_1[i]):
            min = abs(x - list_1[i])
            p = i
        i += 1 
    print(f"\n Самое близкое число к {x} - это {list_1[p]}")