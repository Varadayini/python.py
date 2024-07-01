def password(s,n):
    if n<4:
        return 0
    if  s[0].isdigit():
        return 0
    num=0
    cap=0
    for i in range(n):
        
        if s[i]==" " or s[i]=="/":
            return 0
        elif 'A'<=s[i]<='Z':
           cap+=1
        elif '0'<=s[i]<='9':
            num+=1
    if cap>0 and num>0:
        return 1
    else:
        return 0         
s=input("enter a password")    
n=len(s) 
print(password(s,n))  




        
        
        
