print("Введите длину A")
a=int(input())
print("Введите длину B")
b=int(input())
i=0
t=a
while t>=0:
    t=t-b
print("Незанятая часть отрезка равна", t+b)
