I    = lambda: input()
II   = lambda: int(input())
MII  = lambda: map(int, input().split())
LII  = lambda: list(map(int, input().split()))

def solve():
    n, m = MII()
    grid = [LII() for _ in range(n)]
    
    M = max(max(row) for row in grid)
    
    row_cols = [set() for _ in range(n)]
    col_count = [0]*m
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == M:
                if j not in row_cols[i]:
                    row_cols[i].add(j)
                    col_count[j] += 1
    
    all_cols = [j for j in range(m) if col_count[j] > 0]
    
    for r in range(n):
        if not row_cols[r]:
            continue
        need = 0
        for j in all_cols:
            if col_count[j] - (1 if j in row_cols[r] else 0) > 0:
                need += 1
                if need > 1:
                    break
        if need <= 1:
            return M - 1
    

    return M

t = II()
for _ in range(t):
    print(solve())
