s=["Десять", "Одиннадцать", "Двенадцать", "Тринадцать",
          "Четырнадцать", "Пятнадцать", "Шестнадцать", "Семнадцать",
          "Восемнадцать", "Девятнадцать"]
s1=["Двадцать", "Тридцать", "Сорок"]
s2=[" одно", " два", " три", " четыре", " пять", " шесть", " семь", " восемь", " девять"]
s3=[" учебное задание", " учебных заданий", " учебных задания"]
a=int(input())
if a<10 or a>40:
    print("Не удовлетворяет условиям задачи")
elif 10<= a< 20:
    x=s[a-10]+s3[1]
    print(t)
elif a>=20:
    if a%10==0:
        x=s1[(a//10)-2]+s3[1]
    elif a % 10 == 1:
        x=s1[(a//10)-2]+s2[0]+s3[0]
    elif 1<a%10<5:
            x=s1[(a//10)-2]+s2[a%10-1]+s3[2]
    elif a%10>=5:
            x=s1[(a//10)-2]+s2[a%10-1]+s3[1]
    print(x)
