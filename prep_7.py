n=int(input("enter the no of terms"))

if n<2:
    print(-1)
             
arr=list(map(int,input("enter").split()))
sum=int(input("enter a sum"))
arr=sorted(arr)
    
for i in range(len(arr)-1):
    if arr[i]+arr[i+1] < sum:
        print("the product of two small interger pairs is:",arr[i]*arr[i+1]) 
        break
    
else:
    print(0)
    