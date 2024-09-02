L=-1
R=-1
Lcount=0
Rcount=0
result=0
for i in range(N):
    A,S=input().split()
    A=int(A)

    if S=="L":
        if Lcount==0:
            Lcount+=1
        else:
            result+=abs(L-A)
        L=A
    if S=="R":
        if Rcount==0:
            Rcount+=1
        else:
            result+=abs(R-A)
        R=A
        
print(result)