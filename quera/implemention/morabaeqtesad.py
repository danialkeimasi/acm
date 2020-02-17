import math

n, k = map(int, input().split())
morabas = sum(map(int, input().split()))
print(n - math.ceil(morabas / k))
