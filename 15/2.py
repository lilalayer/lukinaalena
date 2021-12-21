def Sign(x):
    if x<0:
        return -1
    elif x==0:
        return 0
    elif x>0:
        return 1

print("Введите значения А и В")
a=float(input())
b=float(input())
print(Sign(a)+Sign(b))
