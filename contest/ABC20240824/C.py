N=int(input())
katei=list(map(int,input().split()))

H=[0]*len(katei)
for i in range(len(katei)):
    H[i]=katei[i]
now=0
result=0
while True:
    count=H[now]//5
    amari=H[now]%5
    dpresult=result
    if dpresult%3==0:
        if amari==1:
            result+=1
        if amari==2:
            result+=2
        if amari==3 or amari==4:
            result+=3
    elif dpresult%3==1:
        if amari==1:
            result+=1
        if amari==2 or amari==3 or amari==4:
            result+=2
    elif dpresult%3==2:
        if amari==1 or amari==2 or amari==3:
            result+=1
        if amari==4:
            result+=2
    
    result+=count*3
    now+=1
    if now>=N:
        break
print(result)