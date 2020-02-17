fees = list(map(int, input().split()))
times = [0] * 101

for _ in range(3):
    a, b = map(int, input().split())
    for i in range(a, b):
        times[i] += 1

print(sum([times.count(i) * fees[i-1] * i for i in range(1, 4)]))
