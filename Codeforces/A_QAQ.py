I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

s = input()
n = len(s)

# Step 1: Build prefix sums for 'Q'
prefix_q = [0] * (n + 1)

for i in range(n):
    prefix_q[i + 1] = prefix_q[i] + (1 if s[i] == 'Q' else 0)

# Step 2: For each 'A', compute Qs before and after
count = 0
for i in range(n):
    if s[i] == 'A':
        q_before = prefix_q[i]           # 'Q's before index i
        q_after = prefix_q[n] - prefix_q[i + 1]  # 'Q's after index i
        count += q_before * q_after

print(count)
