def lenght(a):
    n=a
    count=0
    while a>0:
        a=a//10
        count+=1
    return count

number=int(input("enter the number"))
n=lenght(number)
number1=number
sum=0
while number>0:
    rem=number%10
    sum=sum+rem**n
    number=number//10

if sum==number1:
    print(number1,"is armstrong")
else :
    print (number1,"is no armstrong")



