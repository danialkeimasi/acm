import math


n, k = map(int, input().split())
print(math.floor(n / math.pow(2, k)))
