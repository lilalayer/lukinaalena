print("Введите длинну массива")
n = int(input())
x = 1
m = []
m1 = []
for i in range(n):
        m.append(x)
        x += 1
print("Изначальный массив", m)
if not (n%2):
    for i in range(1, n//2+1):
        m1.append(m[0])
        m1.append(m[-1])
        m.pop(0)
        m.pop(-1)
    print("Измененный массив", m1)
else:
    for i in range(1, n//2+1):
        m1.append(m[0])
        m1.append(m[-1])
        m.pop(0)
        m.pop(-1)
    m1.append(m[0])
    m.pop(0)
    print("Измененный массив", m1)
