def Quarter(x, y):
    if x>0:
        if y>0:
            return 1
        elif y<0:
            return 4
    elif x<0:
        if y>0:
            return 2
        elif y<0:
            return 3

for i in range(3):
    print("Введите координаты точки через пробел")
    x, y=map(float, input().split())
    print(Quarter(x, y), "четверть")
