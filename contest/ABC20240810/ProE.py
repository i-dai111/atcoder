import sys
readline = sys.stdin.readline

#n = int(readline())
#*a, = map(int, readline().split())

def solve(lst):
    res = [0]*(D+1)
    lst.sort()
    # for i in range(-200,200):
    #     d = 0
    #     for v in lst: d += abs(v-i)
    #     if d <= D:
    #         res[d] += 1
    cnt = 0
    x = -M
    idx = 0
    d = sum(abs(x-i) for i in lst)
    while x <= M:
        #print(x,d,cnt)
        if d <= D: 
            res[d] += 1
        x += 1
        d -= (n-2*cnt)
        while idx < n and lst[idx]==x:
            cnt += 1
            idx += 1
    return res

M = 2*10**6 
n,D = map(int, readline().split())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i],y[i] = map(int,readline().split())

rx = solve(x)
ry = solve(y)
for i in range(1,len(rx)):
    *
    rx[i] += rx[i-1]

ans = 0
for i in range(D+1):
    ans += ry[i]*rx[D-i]
print(ans)





