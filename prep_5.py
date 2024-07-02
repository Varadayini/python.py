n=int(input("enter the digit"))  
m=int(input("enter the number"))      
sum1=0
sum2=0
for i in range(1,m+1):
    if i%n==0:
        sum1+=i
    else:
        sum2+=i
print(abs(sum1-sum2))
        
