n=int(input())
arr=list(map(int,input().split()))
equilibrium=0
for i in range(n):
    if sum(arr[:i])==sum(arr[i+1:]):
        print(arr[:i])
        equilibrium=i+1
        break
if equilibrium==0:
    print("NOT FOUND")
else:
    print(equilibrium)    