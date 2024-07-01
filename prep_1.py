r=int(input("enter the no of rats:"))
unit=int(input("enter the unit:"))
n=int(input("enter the length of array:"))
arr=list(map(int,input().split()))
food_required=r*unit
food_till_now=0
house=0
if n>0:
    for i in range(n):
        food_till_now+=arr[i]
        house+=1
        if food_till_now>=food_required:
            break
    if food_till_now>=food_required:
        print(house)
    else:  
        print(0) 
else:
    print(-1)         
        



