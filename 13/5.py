print("Введите число")
a = int(input())
print("Введите степень")
n = int(input())
su=1
r=1
for i in range(n):
    r *= -a
    su += r
print(su)
