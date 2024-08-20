def main():
    N=int(input())
    S=input()
    counth=0
    countm=0
    for s in S:
        if s=="E":
            countm+=1
        else:
            counth+=1
    result=[0]*len(s)
    result[0]=countm
    for s in S:
        if s=="E":
            result+=1
        else:
            result=-1
    #左端がリーダーの時はresult=countm
if __name__ == "__main__":
    main()