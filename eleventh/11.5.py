print("Введите число")
a=int(input())
if a==0:
    print("Нулевое ", end="")
else:
    if a>0:
        print("Положительное ", end="")
    else:
        print("Отрицательное ", end="")
    if a%2==0:
        print("чётное ", end="")
    else:
        print("нечётное ", end="")
print("число")
