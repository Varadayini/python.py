arr=list(map(int,input("enter").split()))
maxi=0
index=0
for i in range(len(arr)):
    if arr[i]>maxi:
        maxi=arr[i]
        index>i
        index=i
print("maximum element of the array :",maxi)
print("index of that maximum value",index)