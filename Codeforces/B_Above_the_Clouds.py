I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import Counter

inf = float('inf')

def solve():
    n = II()
    s = I()
    c = Counter(s)
    if s[0]==s[-1]:
        for x in c:
            if x==s[0]:
                if c[x]>=3:
                    return True
            else:
                if c[x]>=2:
                    return True
    else:
        for x in c:
            if c[x]>=2:
                return True
        return False

t = II()

for _ in range(t):
    print("Yes" if solve() else "No")