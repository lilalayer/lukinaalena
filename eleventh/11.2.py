print("Введите первое число")
a=int(input())
print("Введите второе число")
b=int(input())
print("Введите третье число")
c=int(input())
if a>c and b>c:
    print(a+b)
elif c>a and b>a:
    print(c+b)
elif a>b and c>b:
    print(c+a)
else:
    print(a+b)
