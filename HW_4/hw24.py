import random

n = int(input("Введите количество кустов n "))

lst = list()

k=0;

for i in range(n):
    k = random.randint(0,5)
    lst.append(k) 
print(lst)
max = lst[-3]+lst[-2]+lst[-1]
while (i < n):
    if lst[i-2]+lst[i-1]+lst[i] > max:
        max = lst[i-2]+lst[i-1]+lst[i]
    i += 1    
if lst[0]+lst[1]+lst[2] > max:
   max = lst[0]+lst[1]+lst[2]
if lst[n-2]+lst[n-1]+lst[0] > max:
    max = lst[n-2]+lst[n-1]+lst[0]
if lst[n-1]+lst[0]+lst[1] > max: 
    max = lst[n-1]+lst[0]+lst[1]         

print(max)