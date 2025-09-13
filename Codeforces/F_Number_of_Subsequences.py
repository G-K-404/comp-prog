I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

MOD1 = 10**9+7

def solve():
    n = II()
    s=I()
    t = "abc"
    def go(i,j):
        if j==3:
            return 1
        if i==n:
            return 0
        ans = 0
        if s[i]==t[j]:
            ans+=(go(i+1,j) + go(i + 1, j + 1))%MOD1 
        elif s[i]=="?":
            # ans+= (3*go(i + 1, j) + go(i + 1, j + 1))%MOD1
            for c in "abc":
                if c==t[j]:
                    ans+=(go(i+1,j) + go(i + 1, j + 1))%MOD1
                else:
                    ans+=(go(i + 1, j))
        else:
            ans+=go(i+1,j)
        ans%=MOD1
        return ans
    return go(0,0)

print(solve())