def main():
    N = int(input())
    
    # 累積和を格納する3次元配列を初期化
    cum_array = [[[0 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
    
    # 累積和を計算
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            A = list(map(int, input().split()))
            for k in range(1, N + 1):
                cum_array[i][j][k] = A[k-1] + cum_array[i-1][j][k] + cum_array[i][j-1][k] + cum_array[i][j][k-1] \
                                      - cum_array[i-1][j-1][k] - cum_array[i-1][j][k-1] - cum_array[i][j-1][k-1] \
                                      + cum_array[i-1][j-1][k-1]
    
    Q = int(input())
    for _ in range(Q):
        B = list(map(int, input().split()))
        A = [b for b in B]
        
        # 累積和を使って範囲の和を高速に計算
        result = cum_array[A[1]][A[3]][A[5]] \
                 - cum_array[A[0] - 1][A[3]][A[5]] \
                 - cum_array[A[1]][A[2] - 1][A[5]] \
                 - cum_array[A[1]][A[3]][A[4] - 1] \
                 + cum_array[A[0] - 1][A[2] - 1][A[5]] \
                 + cum_array[A[0] - 1][A[3]][A[4] - 1] \
                 + cum_array[A[1]][A[2] - 1][A[4] - 1] \
                 - cum_array[A[0] - 1][A[2] - 1][A[4] - 1]
        
        print(result)

if __name__ == "__main__":
    main()