I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

[n,x] = LII()
costs = LII()
pages = LII()
memo = {}

# def dp(ind, remaining_cost):
#     # Base case: no books left
#     if ind == n:
#         return 0
    
#     # Check memoization table
#     if (ind, remaining_cost) in memo:
#         return memo[(ind, remaining_cost)]
    
#     # Option 1: Skip the current book
#     option1 = dp(ind + 1, remaining_cost)
    
#     # Option 2: Include the current book (only if cost allows)
#     option2 = 0
#     if costs[ind] <= remaining_cost:
#         option2 = pages[ind] + dp(ind + 1, remaining_cost - costs[ind])
    
#     # Store the result in the memo table and return the maximum value
#     memo[(ind, remaining_cost)] = max(option1, option2)
#     return memo[(ind, remaining_cost)]


# # Run the DP function
# print(dp(0, x))

def go(cost, i):
    if i >= n:
        return 0
    ans = go(cost, i + 1) 
    if cost + costs[i] <= x:
        ans = max(ans, go(cost + costs[i], i + 1) + pages[i]) 
    return ans
print(go(0,0))

