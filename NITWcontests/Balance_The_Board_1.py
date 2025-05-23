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
    s1 = I()
    s2 = I()
    count = {'R': 0, 'W': 0, '?': 0}
    rlock = [0]*2
    wlock = [0]*2
    for i in range(n):
        if(s1[i]==s2[i] and s1[i]!='?'):
            print(-1)
            return
        if((s1[i] == '?' or s2[i] == '?') and s1[i]!=s2[i]):
            if(s1[i] == '?'):
                if(s2[i]=='R'):
                    wlock[0] +=1
                if(s2[i] == 'W'):
                    rlock[0] += 1
            if(s2[i] == '?'):
                if(s1[i]=='R'):
                    wlock[1] +=1
                if(s1[i] == 'W'):
                    rlock[1] += 1
        else:
            count[s1[i]] +=1
    if((abs(count['R']+rlock[0]-count['W']-wlock[0])<=count['?'])):
        print(abs(count['R']-count['W'])+abs(count['R']-count['W'])-(sum(rlock)+sum(wlock)))
        return
    else:
        print(-1)
        return

solve()