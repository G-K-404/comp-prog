I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


n = II()
ticket = I()
arr = list(map(int,ticket))
s = sum(arr)
def solve():
    if arr.count(0)==n:
        print("YES")
        return
    for k in range(1,s):
        ts = 0
        parts = 0
        idx = 0
        for x in arr:
            ts+=x
            idx+=1
            if ts==k:
                parts+=1
                ts = 0
            if ts>k:
                break
        if parts>=2 and ts==0 and idx==n:
            print("YES")
            return
        
    print("NO")
solve()