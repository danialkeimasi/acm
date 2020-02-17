n = int(input())
nodes = {i:0 for i in range(1, n + 1)}

for i in range(n-1):
    m, n = map(int, input().split())
    nodes[m] += 1
    nodes[n] += 1

print(max(nodes.values()))
