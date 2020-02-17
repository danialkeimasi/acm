n = int(input())


numbers = []
for i in range(1, n+1):
    numbers += [i]
    for j in range(1, i//2 + 1):
        if i % j == 0:
            numbers.append(j)

print(len(numbers), sum(numbers))
