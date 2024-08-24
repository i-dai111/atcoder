N,K=map(int,input().split())
K=K-1
A=list(map(int,input().split()))
c=0
for i in range(K+1):
    print(A[N-K+i-1],end=' ')
for i in range(N-K-1):
    print(A[i],end=' ')