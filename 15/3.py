def RingS(r1, r2):
    s=3.14*(r1**2-r2**2)
    return s
print("Введите радиус большего кольца")
r1=float(input())
print("Введите радиус меньшего кольца")
r2=float(input())
print("Площадь кольца равна:", RingS(r1, r2))
