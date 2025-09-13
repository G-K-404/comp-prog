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
    s = I()
    s1 = list(set(s))
    s1.sort()
    s2 = s1[::-1]
    d = {}
    for i in range(len(s1)):
        d[s1[i]] = s2[i]
    temp = list(s)
    for i in range(len(temp)):
        temp[i] = d[temp[i]]
    print("".join(temp))


t = II()

for _ in range(t):
    solve()