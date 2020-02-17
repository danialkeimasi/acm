n = int(input())
names = [len(set(name)) for name in [input() for i in range(n)]]
print(max(names))
