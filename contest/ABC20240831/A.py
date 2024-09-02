A,B=map(int,input().split())

result=2

if abs(A-B)%2==0:
    result+=1

if A-B==0:
    result=1

print(result)