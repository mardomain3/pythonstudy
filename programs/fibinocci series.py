n=int(input("enter the range"))
f=0
s=1
print(f)
print(s)
for i in range(2,n):
    temp=s
    s=f+s
    f=temp
    print(s)
