import random
n= int(input("Введите количество монеток "))
i = 0
side = 0
count0 = 0
count1 = 0
while(i < n):
    side = random.randint(0,1)
    print(side, end = " ")
    if (side == 0):
        count0 += 1
    if (side == 1):
        count1 += 1
    i += 1
if(count0<count1): 
    print(f"\n Минимальное число {count0}")
if (count0>count1): 
    print(f"\n Минимальное число {count1}")

