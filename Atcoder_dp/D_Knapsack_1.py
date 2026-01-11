I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

# def solve():
#     [n, w] = LII()
#     items = []
#     for i in range(n):
#         temp = LII()
#         items.append(temp)
#     dp = [[0]*(w+1) for i in range(n+1)]
#     netval = -1
#     for i in range(n):
#         for sw in range(1,w+1):
#             if(sw - items[i][0] >= 0):
#                 dp[i+1][sw] = max(dp[i+1][sw], dp[i][sw - items[i][0]] + items[i][1])
#             dp[i+1][sw] = max(dp[i+1][sw], dp[i][sw])
#     print(dp[n][w])
# solve()

def solve():
    n,w = MII()
    items = []
    for _ in range(n):
        items.append(LII())
    # def go(netwt, i):
    #     if i>=n:
    #         return -inf
    #     if i==n-1:
    #         netwt+=items[i][0]
    #         if netwt>w:
    #             return 0
    #         return items[i][1]

    #     if netwt>w:
    #         return -inf
    #     a = go(netwt+items[i][0],i+1)+items[i][1]
    #     b = go(netwt, i+1)
    #     return max(a,b)
    # return go(0,0)
    dp = [[-inf]*n  for _ in range(w+1)]
    for i in range(n-1,-1,-1):
        for wt in range(w):
            if wt+items[i][0]<=w:
                dp[i][wt] = max(dp[i][wt], dp[i+1][wt+items[i+1][0]+items[i+1][1]])
print(solve())

#state: total weight accumulated so far and current item
#transition: take current item and update cost or skip current item
#base case: if all items have been iterated
#final result maximum value obatained with weight less than or equal to threshold