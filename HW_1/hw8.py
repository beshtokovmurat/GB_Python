print("Введите размеры шоколада n*m")
print("Введите n")
n= int(input())
print("Введите m")
m= int(input())
print("Введите число к <= n*m")
k= int(input())
print(k%n)
if (k%n==0) or (k%m==0):
    print("Yes")
else:
    print("No")
if (k>n*m):
    print("No")
