print("Введите трехзначное число ")
n= int(input())
n1 = n//10
print(f"Сумма цифр = {n % 10 + n1%10 +n// 100}")