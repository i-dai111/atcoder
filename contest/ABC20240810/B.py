
def rearrange_input(inputs):
    # 文字列を列ごとに分解
    columns = [list(col) for col in zip(*inputs)]

    # 各列をソートし、末尾に`*`が入らないように空白で埋める
    rearranged_columns = []
    for col in columns:
        sorted_col = sorted(col)
        rearranged_columns.append(''.join(sorted_col).rstrip('*'))
    
    # 各列を再構成して出力
    return '\n'.join(''.join(row).rstrip('*') for row in zip(*rearranged_columns))


def main():
    # 入力を読み取る
    strings = []
    N=int(input())
    while True:
        try:
            line = input().strip()
            if line:
                strings.append(line)
            else:
                break
        except EOFError:
            break
    
    # 並び替えを実行
    print(rearrange_input(strings))

if __name__ == "__main__":
    main()