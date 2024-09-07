def find_min_steps(s1, s2):
    # s1: 初期文字列
    # s2: 目標文字列
    X = []  # 初期状態を配列に追加
    
    # 1文字ずつ変更していく
    for i in range(len(s1)):
        if s1[i] > s2[i]:
            # 文字列のi番目をs2の対応する文字に置き換える
            s1 = s1[:i] + s2[i] + s1[i+1:]
            X.append(s1)
    for i in reversed(range(len(s1))):
        if s1[i] < s2[i]:
            # 文字列のi番目をs2の対応する文字に置き換える
            s1 = s1[:i] + s2[i] + s1[i+1:]
            X.append(s1)
    
    return X

# 入力
s1 = input().strip()
s2 = input().strip()

# 最小要素数で辞書順最小の配列Xを求める
result = find_min_steps(s1, s2)

# 出力
print(len(result))
for x in result:
    print(x)