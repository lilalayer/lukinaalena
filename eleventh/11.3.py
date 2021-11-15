print("Введите координату точки A")
a=int(input())
print("Введите координату точки B")
b=int(input())
print("Введите координату точки C")
c=int(input())
if abs(a-b)<abs(a-c):
    print("Точка B ближе к точке A. Расстояние равно", abs(a-b))
elif abs(a-b)>abs(a-c):
    print("Точка C ближе к точке A. Расстояние равно", abs(a-c))
