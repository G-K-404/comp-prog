I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')






n = II()
lis = LII()
def iterate(A):
    n = len(A)
    A = [0] + A
    
    for i in range(1, n):
        if i % 2 == 0 and A[i] == 1 and A[i + 1] == 0:
            A[i], A[i + 1] = A[i + 1], A[i]
        elif i % 2 == 1 and A[i] == 0 and A[i + 1] == 1:
            A[i], A[i + 1] = A[i + 1], A[i]
    
    ans = 0
    for i in range(1, n + 1):
        if i % 2 == 0 and A[i] == 0:
            ans += 1
        elif i % 2 == 1 and A[i] == 1:
            ans += 1
    
    return ans

print(iterate(lis))
