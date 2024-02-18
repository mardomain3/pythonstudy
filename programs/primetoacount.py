n=int(input("enter the range"))
count=0
i=2
while count<n:

        for j in range(2,i):
            if i % j==0:
                break
        else :
            print(i)
            count+=1
        i=i+1