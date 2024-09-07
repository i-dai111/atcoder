H, W, Q = map(int, input().split())
Grid = [[1 for j in range(W)] for i in range(H)]  # 初期状態を全て1に設定

# 再帰的に処理する関数を定義
def recursive_zero(R, C, direction):
    if direction == 'up' and R > 0 and Grid[R-1][C] == 0:
        if R > 1:
           
            recursive_zero(R-1, C, 'up')  # 上に向かって再帰
    else:
        if R >= 1:
            Grid[R-1][C] = 0

    if direction == 'down' and R < H-1 and Grid[R+1][C] == 0:
        if R < H-2:
           
            recursive_zero(R+1, C, 'down')  # 下に向かって再帰
    else:
        if R =< H-2:
            Grid[R+1][C] = 0

            
    if direction == 'left' and C > 0 and Grid[R][C-1] == 0:
        if C > 1:
            
            recursive_zero(R, C-1, 'left')  # 左に向かって再帰
    else:
        if C >= 1:
            Grid[R][C-1] = 0


    if direction == 'right' and C < W-1 and Grid[R][C+1] == 0:
        if C < W-2:
            recursive_zero(R, C+, 'right')  # 右に向かって再帰
    else:
        if C =< W-2:
            Grid[R][C+1] = 0

for i in range(Q):
    R, C = map(int, input().split())
    R -= 1  # 1-originから0-originに変換
    C -= 1  # 1-originから0-originに変換
    
    # もしグリッドが1なら0に、0なら1に変更
    if Grid[R][C] == 1:
        Grid[R][C] = 0
    else:
        # 上下左右のチェック
        if R > 0 and Grid[R-1][C] == 1:  # 上
            Grid[R-1][C] = 0
        if R > 0 and Grid[R-1][C] == 0:
            recursive_zero(R-1, C, 'up')  # 再帰的に上方向へ


        if R < H-1 and Grid[R+1][C] == 1:  # 下
            Grid[R+1][C] = 0
        if R < H-1 and Grid[R+1][C] == 0:
            recursive_zero(R+1, C, 'down')  # 再帰的に下方向へ


        if C > 0 and Grid[R][C-1] == 1:  # 左
            Grid[R][C-1] = 0
        if C > 0 and Grid[R][C-1] == 0:  
            recursive_zero(R, C-1, 'left')  # 再帰的に左方向へ


        if C < W-1 and Grid[R][C+1] == 1:  # 右
            Grid[R][C+1] = 0
        if C < W-1 and Grid[R][C+1] == 0:
            recursive_zero(R, C+1, 'right')  # 再帰的に右方向へ

# 最終的なグリッドの中で1の数をカウント
count_ones = sum(row.count(1) for row in Grid)
print(count_ones)

