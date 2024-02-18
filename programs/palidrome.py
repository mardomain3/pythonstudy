word=input("enter the word ")
wordrev=word[::-1] #reversed the string using sliding technique

if word==wordrev:
    print("palidrome")
else:
    print("not palidrome")