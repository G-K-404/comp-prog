import sys
input = sys.stdin.readline
from collections import defaultdict

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

pxor = [0]
x = 0
for num in arr:
    x ^= num
    pxor.append(x)

all_vals = set(pxor)
for val in pxor:
    all_vals.add(val ^ k)

compressed = {val: idx for idx, val in enumerate(sorted(all_vals))}
pxor = [compressed[val] for val in pxor]

BLOCK = int(n ** 0.5)
queries = []
for i in range(m):
    l, r = map(int, input().split())
    queries.append((l, r, i))

queries.sort(key=lambda x: ((x[0] // BLOCK, x[1]) if (x[0] // BLOCK) % 2 == 0 else (x[0] // BLOCK, -x[1])))

cnt = 0
answers = [0] * m
freq = [0] * (2 * n + 10)
curr_l = 1
curr_r = 0
freq[pxor[0]] = 1

for l, r, idx in queries:
    while curr_r < r:
        curr_r += 1
        val = pxor[curr_r]
        cnt += freq[val ^ compressed[k]]
        freq[val] += 1

    while curr_r > r:
        val = pxor[curr_r]
        freq[val] -= 1
        cnt -= freq[val ^ compressed[k]]
        curr_r -= 1

    while curr_l < l:
        val = pxor[curr_l - 1]
        freq[val] -= 1
        cnt -= freq[val ^ compressed[k]]
        curr_l += 1

    while curr_l > l:
        curr_l -= 1
        val = pxor[curr_l - 1]
        cnt += freq[val ^ compressed[k]]
        freq[val] += 1

    answers[idx] = cnt

print('\n'.join(map(str, answers)))
