<<<<<<< HEAD
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
sus = LII()

def go(i,)
=======
from functools import lru_cache

I = lambda: input()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

n = II()
a = LII()

one = a.count(1)
two = a.count(2)
three = a.count(3)

@lru_cache(maxsize=None)
def go(one, two, three):
    if one == 0 and two == 0 and three == 0:
        return 0.0
    res = 1 
    if one > 0:
        res += one / n * go(one - 1, two, three)
    if two > 0:
        res += two / n * go(one + 1, two - 1, three)
    if three > 0:
        res += three / n * go(one, two + 1, three - 1)
    res /= (one + two + three) / n
    return res
print(go(one,two,three))
>>>>>>> 2f6612852ebc014714fb29b63627e467478aa78c
