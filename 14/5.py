print("Введите число")
a = int(input())
print("Введите второе число")
b = int(input())
while a != b:
    t = sorted([a, b])
    a, b = t[1] - t[0], t[0]
print("Наибольший общий делитель:", a)
