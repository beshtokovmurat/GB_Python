def sum(a,b):
    if b == 0:
        return a
    elif a == 0:
        return b
    elif a >= b:
        return(a + sum(1,b-1))
    return(b + sum(a-1,1))
A = int(input("Введите неотрицательное число A "))
B = int(input("Введите неотрицательное число B "))
print(sum(A,B))