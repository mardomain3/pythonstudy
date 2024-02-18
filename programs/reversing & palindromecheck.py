n=int(input("enter the number"))
temp=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10

print("reversed number is",rev)

j=input("do u want to check whether the number is palidrome or not(yes or not)")
if j=="YES" or j=="yes":
    if temp==rev:
        print(temp,"is palidrome")
    else:
        print(temp,"is not a palidrome")
