n=int(input())
arr=list(map(int,input().split()))
product=int(input())
unique_triplets=[]
count=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]*arr[j]*arr[k]==product:
                triplet=sorted([arr[i],arr[j],arr[k]])
                if triplet not in unique_triplets:
                    unique_triplets.append(triplet)
                    count+=1
print(count)                    
            
