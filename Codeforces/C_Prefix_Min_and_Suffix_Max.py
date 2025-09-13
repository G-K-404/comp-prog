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
    lis = LII()
    prefmin = [0]*n
    sufmax = [0]*n
    prefmin[0] = lis[0]
    for i in range(1, n):
        prefmin[i] = min(prefmin[i-1], lis[i])
    sufmax[-1] = lis[-1]
    for i in range(n-2, -1, -1):
        sufmax[i] = max(sufmax[i+1], lis[i])
    ans = []
    for i in range(n):
        if (i == 0 or prefmin[i-1] > lis[i]) or (i == n-1 or sufmax[i+1] < lis[i]):
            ans.append('1')
        else:
            ans.append('0')
    print(''.join(ans))

t = II()
for _ in range(t):
    solve()