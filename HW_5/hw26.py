def power(a,b):
    if b == 1:
        return a
    return(a*power(a,b-1))

A = int(input("Введите число A "))
B = int(input("Введите число B "))
print(power(A,B))