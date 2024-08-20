def change(op, n):
    if op == 0:
        return n
    elif op == 1:
        return -n

def main():
    A, B, C, D = map(int, input())
    found = False  # ループを抜けるためのフラグ
    for op1 in range(2):
        for op2 in range(2):
            for op3 in range(2):
                if A + change(op1, B) + change(op2, C) + change(op3, D) == 7:
                    print(A, end='')
                    if op1 == 0:
                        print("+", end='')
                    else:
                        print("-", end='')
                    print(B, end='')
                    
                    if op2 == 0:
                        print("+", end='')
                    else:
                        print("-", end='')
                    print(C, end='')

                    if op3 == 0:
                        print("+", end='')
                    else:
                        print("-", end='')
                    print(D, end='')

                    print("=7", end='')
                    found = True
                    break  # 内側のループから抜ける
            if found:
                break  # 中間のループから抜ける
        if found:
            break  # 最外のループから抜ける

if __name__ == "__main__":
    main()