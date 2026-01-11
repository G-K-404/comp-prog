<<<<<<< HEAD
MOD = 10 ** 9 + 7

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    prefix = [0] * (k + 2)
    for j in range(k + 1):
        prefix[j + 1] = (prefix[j] + dp[j]) % MOD
    
    new_dp = [0] * (k + 1)
    for j in range(k + 1):
        l = j - a[i]
        if l < 0:
            new_dp[j] = prefix[j + 1]
        else:
            new_dp[j] = (prefix[j + 1] - prefix[l]) % MOD
    dp = new_dp

print(dp[k])
=======
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n,k = MII()
a = LII()

>>>>>>> 2f6612852ebc014714fb29b63627e467478aa78c
