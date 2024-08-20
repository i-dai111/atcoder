import itertools

def generate_combinations(N,K,R):
    # 各位置における範囲を指定
    ranges = [range(1,R[n]+1) for n in range(0, N)]
    # 全ての組み合わせを生成
    combinations = list(itertools.product(*ranges))
    
    # 辞書順にソート
    combinations.sort()
    
    # 結果を出力
    for combo in combinations:
      if sum(combo)%K==0:
        print(' '.join(map(str, combo)))

def main():
    N,K=map(int,input().split())
    R=list(map(int,input().split()))
    generate_combinations(N,K,R)
if __name__ == "__main__":
    main()

