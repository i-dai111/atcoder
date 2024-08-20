def main():
    N, D = map(int,input().split())
    X=[0]*N
    Y=[0]*N
    for n in range(N):
        x, y = map(int,input().split())
        X[n]=x
        Y[n]=y
    maxX=max(X)
    minX=min(X)
    minY=min(Y)
    maxY=max(Y)
    rangeX=maxX-minX
    rangeY=maxY-minY
    count=0
    for i in range(minX,maxX+1):
        for j in range(minY,maxY+1):
            result=0
            for x,y in zip(X,Y):
                result+=abs(x-i)+abs(y-j)
            if result<=D:
                count+=1
    print(count)

if __name__=="__main__":
    main()
import sys
s= -M