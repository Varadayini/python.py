
def number_of_carries(n1,n2):
    carry=0
    count=0
    while n1>0 or n2>0:
        digit1=n1%10
        digit2=n2%10
        sum=digit1+digit2+carry
        if sum>=10:
            count+=1
            carry=1
            
        else:
            carry=0  
        n1//=10
        n2//=10
    return count        
n1=int(input("enter:"))
n2=int(input("enter:"))
print(number_of_carries(n1,n2))
