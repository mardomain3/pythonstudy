word=input("enter the word")
word=word.upper()
ca=0
ce=0
ci=0
co=0
cu=0

for i in range(len(word)):
    if word[i]=="A":
        ca+=1
    elif word[i]=="I":
        ci+=1
    elif word[i]=="O":
        co+=1
    elif word[i]=="E":
        ce+=1
    elif word[i]=="U":
        cu+=1
    else: continue
print("TOTAL NO OF VOWELS:",ca+ce+ci+co+cu)
print("NO OF A'S:",ca)
print("NO OF E'S:",ce)
print("NO OF I'S:",ci)
print("NO OF O'S:",co)
print("NO OF U'S:",cu)