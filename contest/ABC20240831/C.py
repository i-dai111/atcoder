N=int(input())

A=list(map(int,input().split()))

if N==1:
    print("1")
    exit()
d=A[1]-A[0]

continuous=1
result=0
for i in range(len(A)-1):
    if d==A[i+1]-A[i]:
        continuous+=1
    else:
        result+=continuous*(continuous+1)*(1/2)
        continuous=2
        result-=1

    d=A[i+1]-A[i]

result+=continuous*(continuous+1)*(1/2)

print(int(result))