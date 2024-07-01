arr=list(map(int,input().split()))
no=int(input("enter a number"))
diff=int(input("enter a difference value"))
c=0

for i in range(len(arr)):
    if(abs(arr[i]-no)<=diff):
        c+=1
if c==0:
    print(-1)        
else:  
    print(c)   