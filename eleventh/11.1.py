print("Введите переменную A")
a=int(input())
print("Введите переменную B")
b=int(input())
if a==b:
    a=0
    b=0
else:
    if a>b:
        b=a
    else:
        a=b
print(a, b)
