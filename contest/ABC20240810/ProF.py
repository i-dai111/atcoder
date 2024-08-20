import sys
readline = sys.stdin.readline

#n = int(readline())
#*a, = map(int, readline().split())
def sorted_by_atan2(lst):
    upper = [] # 上半平面
    lower = [] # 下半平面
    pos = []   # 非負軸
    neg = []   # 負軸
    f = lambda xy: (xy[0]<<64)//abs(xy[1])
    for xy in lst:
        if xy[1] > 0:
            upper.append(xy)
        elif xy[1] < 0:
            lower.append(xy)
        elif xy[0] < 0:
            neg.append(xy)
        else:
            pos.append(xy)
    upper.sort(key=lambda xy: (-xy[0]<<64)//xy[1])
    lower.sort(key=lambda xy: (xy[0]<<64)//-xy[1])
    return lower + pos + upper + neg

n,k = map(int, readline().split())
res = []
for _ in range(n):
    a,b = map(int, readline().split())
    res.append((a-1,b))

#res.sort(key=lambda lst:lst[1]/lst[0],reverse=1)
res = sorted_by_atan2(res)[::-1]
#print(res)

INF = -1<<60
dp = [INF]*(k+1)
dp[0] = 1
for a,b in res:
    for i in range(1,k+1)[::-1]:
        dp[i] = max(dp[i],dp[i-1]*(a+1)+b)
print(dp[-1])

