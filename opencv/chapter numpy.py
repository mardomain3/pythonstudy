import numpy as np

arr1=np.array([(1,2),(3,4),(5,6)])
print(arr1)
arr2=np.ones((3,4),dtype="int")
print(arr2)
print(arr1.dtype)
arr3=np.zeros((2,3),dtype="uint8")
print(arr3)
arr4=np.eye(3,dtype="int")
print(arr4)
arr5=np.linspace(0,10,9,dtype="int")
print(arr5)
arr6=np.arange(0,20,2)
print(arr6)
arr7=np.logspace(2,20,5)
print(arr7)

print(arr1.shape)
print(arr1.size)
arr8=np.empty((2,3),dtype="int")
for i in range(2):
    for j in range(3):
        arr8[i][j]=int(input("enter the value"))

print(arr8)


