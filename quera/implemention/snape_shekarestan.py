n, m = map(int, input().split())

prices = {}
for i in range(n):
    prices.update(
        {(i+1, j+1): int(des) for j, des in enumerate(input().split())}
    )

print(sum([prices[tup] for tup in [tuple(map(int, input().split())) for _ in range(m)]]))
