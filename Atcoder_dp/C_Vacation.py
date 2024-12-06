I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


def solve():
    n = II()
    a = []
    for _ in range(n):
        tem = LII()
        a.append(tem)
    dp = [[-inf] * 3 for _ in range(n+1)]
    dp[0] = [0,0,0]
    for i in range(n):
        for j in range(3):
            for k in range(3):
                if(j==k):
                    continue
                dp[i+1][k] = max(dp[i+1][k], dp[i][j]+a[i][k])
    return max(dp[n])
print(solve())