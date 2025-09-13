I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def min_boredom_value(n, m, arr):
    def compute_cost(x):
        cost = 0
        for a in arr:
            mod_val = a % m
            if mod_val <= x:
                cost += x - mod_val
            else:
                cost += x+m - mod_val
        return cost

    left, right = 0, m 
    min_cost = float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        cost_mid = compute_cost(mid)
        cost_mid_plus_one = compute_cost(mid + 1) if mid + 1 < m else float('inf')
        min_cost = min(min_cost, cost_mid)
        if cost_mid <= cost_mid_plus_one:
            right = mid - 1
        else:
            left = mid + 1
    
    return min_cost
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_boredom_value(n, m, arr))
