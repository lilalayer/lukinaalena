r=0
print("Введите целое число N")
n=int(input())
print("Введите число A")
a=float(input())
for i in range(0,n+1):
    r+=a**i
print(r)
