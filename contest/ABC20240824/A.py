N,K=map(int,input().split())
K=K-1
A=list(map(int,input().split()))
c=0
for i in range(len(A)):
    if i+K<len(A):
        print(A[i+K],end=' ')
    else:
        print(A[c],end=' ')
        c+=1
