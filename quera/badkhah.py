import itertools

p, d = map(int, input().split())

for i in itertools.count(1):
    if 0 <= (i * d) % p <= p//2:
        print(i * d)
        break
