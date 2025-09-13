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
    n2 = II()
    for _ in range(n2):
        s = I()
        if(len(s) != len(lis)):
            print("NO")
            continue
        dic = {}
        for i in range(n):
            if s[i] not in dic:
                dic[s[i]] = lis[i]
            else:
                if(dic[s[i]] != lis[i]):
                    print("NO")
                    break
            if(i == n-1):
                print("YES")


t = II()
for _ in range(t):
    solve()