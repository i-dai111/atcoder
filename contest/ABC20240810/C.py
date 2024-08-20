def main():
    Q=int(input())
    X=[0]*10**6
    count=0
    for i in range(Q):
        query=list(map(int, input().split()))
        if query[0]==1:
            if X[query[1]-1]==0:
                count+=1
            X[query[1]-1]+=1
            
        if query[0]==2:
            if X[query[1]-1]==1:
                count-=1
            X[query[1]-1]-=1
        if query[0]==3:
            print(count)
            
    



if __name__=="__main__":
    main()