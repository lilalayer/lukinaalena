print("Введите сторону A")
a=int(input())
print("Введите сторону B")
b=int(input())
print("Введите сторону C")
c=int(input())
if (a+b>c) and (b+c>a) and (c+a>b):
    print("Высказывание истинно")
else:
    print("Высказывание ложно")
