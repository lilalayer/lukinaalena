print("Введите длину массива")
n=int(input())
print("Введите первый элемент массива")
a=int(input())
print("Введите знаменатель геометрической прогрессии")
d=int(input())
m=[a]
for i in range(n-1):
    x=m[i]
    x*=d
    m.append(x)
print(m)
