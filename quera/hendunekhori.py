_ = int(input())
arr = list(map(int, input().split()))
decode = {item: i+1 for i, item in enumerate(arr)}

while len(arr) > 1:
    arr.remove(min(arr[0:2]))

print(decode[arr[0]])
