N=int(input())

A= [[] for _ in range(100)]

for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(len(tmp)):
      A[i].append(tmp[j]-1)
L=0

for i in range(N):
    if L>=i:
        L=A[L][i]
    else:
        L=A[i][L]

print(L+1) 