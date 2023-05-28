import math

n = int(input("Введите любое числo "))
i = 0
k = 1
print("Все целые степени двойки < n")
while(i < n):
    i = math.pow(2,k)
    print(math.pow(2,k-1), end=" ")
    k += 1
print("\n") 
