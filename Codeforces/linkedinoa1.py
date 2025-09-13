I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import defaultdict

inf = float('inf')
def getMinOperations(change, arr):
    m = len(arr)
    null_count = 0
    n = len(change)

    # Keep track of which indexes are NULL
    is_null = [False] * m

    for i in range(n):
        idx = change[i]

        if idx == 0:
            # decrement any non-null element if possible
            for j in range(m):
                if not is_null[j]:
                    arr[j] -= 1
                    if arr[j] == 0:
                        is_null[j] = True
                        null_count += 1
                    break
        else:
            idx -= 1  # convert to 0-based index
            if not is_null[idx]:
                arr[idx] -= 1
                if arr[idx] == 0:
                    is_null[idx] = True
                    null_count += 1

        if null_count == m:
            return i + 1  # operations are 1-based count

    return -1


n = II()
change = []
for _ in range(n):
    change.append(II())
m = II()
arr = []
for _ in range(m):
    arr.append(II())
print( getMinOperations(change, arr))