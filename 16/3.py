print("Введите длину массива")
n=int(input())
print("Введите A - первый элемент массива")
a=int(input())
print("Введите B - второй элемент массива")
b=int(input())
if n<3:
    print("Задача не может быть выполнена")
if n>2:
    m=[a, b]
    for i in range(n-2):
        s=sum(m)
        m.append(s)
    print(m)
    
