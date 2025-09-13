def find_missing_number_binary_search():
    # Read input
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    left, right = 0, n - 2
    
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1
    print(left + 1)

find_missing_number_binary_search()
