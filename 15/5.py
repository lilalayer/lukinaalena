def Fact2(n):
    f=1
    if n%2==0:
        for i in range(2, n+1, 2):
            f*=i
        return f
    elif n%2!=0:
        for i in range(1, n+1, 2):
            f*=i
        return f

print("Введите N")
n=int(input())
print(Fact2(n))   
