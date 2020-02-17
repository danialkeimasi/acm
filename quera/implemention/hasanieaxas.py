n, k = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
while i < len(arr) - 1:
    test_key = arr[i] + arr[i+1]
    if test_key <= k:
        arr[i] = test_key
        arr.pop(i+1)
    else:
        i += 1

print(len(arr))
