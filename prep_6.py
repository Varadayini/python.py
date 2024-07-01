l=int(input("enter a length"))
even=[]
odd=[]

if l>3:
    n=list(map(int,input("enter").split()))
    for i in range(l):
        if i%2==0:
            even.append(n[i])
        else:
            odd.append(n[i])   
    even=sorted(even)
    print(even)          # for understanding purpose
    odd=sorted(odd)
    print(odd)             # for understanding purpose
    print(even[-2]+odd[1])
else:
    print(0)

        
