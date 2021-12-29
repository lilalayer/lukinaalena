print("Введите размер массива:")
n = int(input())
x = 1
m = []
m1 = []
m2 = []
itog = []
for i in range(n):
    m.append(x)
    x += 1
print("Изначальный массив", m)
for i in range(len(m)):
    if i % 2 == 0:
        m2.append(m[i])
    else:
        m1.append(m[i])
m2 = sorted(m2)
m1 = reversed(sorted(m1))
for i in m2:
    itog.append(i)
for i in m1:
    itog.append(i)

print("Измененный массив", itog)
