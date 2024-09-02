def max_sum(A):
    n = len(A)
    
    if n == 0:
        return 0
    
    # dp[i][0] : i 番目まで選んで奇数回目の選択をしたときの最大合計
    # dp[i][1] : i 番目まで選んで偶数回目の選択をしたときの最大合計
    dp = [0] * 2
    
    # 初期条件
    dp[0] = A[0]  # 最初の選択が奇数回目
    dp[1] = -float('inf')  # 最初の選択が偶数回目は無効
    
    for i in range(1, n):
        new_dp = [0] * 2
        # 奇数回目の選択
        new_dp[0] = max(dp[0], dp[1]) + A[i]
        # 偶数回目の選択
        new_dp[1] = max(dp[0], dp[1]) + 2 * A[i]
        
        dp = new_dp
    
    # 最大合計を求める
    return max(dp[0], dp[1])

N=int(input())
# 入力を取得
A = list(map(int, input().split()))

# 最大合計を計算して出力
print(max_sum(A))