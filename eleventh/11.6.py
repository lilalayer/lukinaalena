print("Введите число")
a=int(input())
if a%2==0:
    print("Чётное", end=" ")
else:
    print("Нечётное", end=" ")
if a<10:
    print("однозначное", end=" ")
if a>=10 and a<100:
    print("двузначное", end=" ")
if a>=100:
    print("трёхзначное", end=" ")
print("число")
