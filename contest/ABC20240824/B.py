N=int(input())
r=list(map(int,input().split()))
A=[0]*len(r)
for i in range(len(r)):
    A[i]=r[i]
result=0
while True:
    A=sorted(A, reverse=True)
    if A[1]==0:
        break
    A[0]-=1
    A[1]-=1
    result+=1
print(result)
    