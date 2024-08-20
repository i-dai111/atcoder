def main():
    N,T,A=map(int,input().split())
    kahan=N//2 + 1
    if kahan <= T or kahan <= A:
        print("Yes")
    else:
        print("No")
if __name__=="__main__":
    main()
    