import math

s = int(input("Введите сумму чисел "))
p = int(input("Введите произведение чисел "))
b1 = (s - math.sqrt(s*s - 4*p))/2
a1 = s - b1
b2 = (s + math.sqrt(s*s - 4*p))/2
a2 = s - b2
if (s*s - 4*p > 0 and b1 > 0 and b1 != b2):
    print(f"Задуманные числа: ({a1}, {b1}) и ({a2}, {b2})")
if (s*s - 4*p == 0):
    print(f"Задуманные числа: ({a1}, {b1})")
if (s*s - 4*p < 0):
    print(f"Невозможно представить") 
