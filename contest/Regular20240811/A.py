def main():
    N,Q=map(int,input().split())
    S=[0]*N
    P=[0]*Q
    V=[0]*Q

    for i in range(Q):
        P[i],V[i]=map(int,input().split())
    for i in range(Q):
        P[i]=P[i]-1
if __name__ == "__main__":
    main()