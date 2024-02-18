n=int(input("enter the range"))

def fib (a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fib(a-1)+fib(a-2)

for i in range(n):
    print(fib(i) ,end=" ")