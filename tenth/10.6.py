print("Введите сторону A")
a=int(input())
print("Введите сторону B")
b=int(input())
print("Введите сторону C")
c=int(input())
if a**2+b**2==c**2:
    print("Высказывание истинно")
elif a**2+c**2==b**2:
    print("Высказывание истинно")
elif b**2+c**2==a**2:
    print("Высказывание истинно")
else:
    print("Высказывание ложно")
    
