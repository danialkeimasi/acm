import collections

xs, ys = [], []
for i in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

print(collections.Counter(xs).most_common()[-1][0], collections.Counter(ys).most_common()[-1][0])
