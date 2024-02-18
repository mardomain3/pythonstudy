word=input("enter the text ")
a=int(input("enter the distance"))
z=ord("z")
aa=ord("a")
for i in word:
    temp=ord(i)
    if temp+a<=z:
        temp=temp+a
    else :
        temp=aa+temp%z
    print(chr(temp),end="")

