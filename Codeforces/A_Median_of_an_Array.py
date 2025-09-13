I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def med_changer(med, list, ind, counts):
    list[ind] += 1
    counts+=1
    list.sort()
    if(list[ind] == med+1):
        return counts
    else:
        return med_changer(med, list, ind, counts)

    

def solve():
    n = II()
    inp = LII()
    l = 0
    if(n%2 == 0):
        l = int(n/2)-1
    else:
        l = int(n/2)
    inp.sort()
    med = inp[l]
    counts = 0
    count = med_changer(med, inp, l, counts)
    print(count)

t = II()
for _ in range(t):
    solve()