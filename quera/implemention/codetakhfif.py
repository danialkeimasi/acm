n, valid = input().split()
n, valid = int(n), set(valid)

codes = [set(input()) for i in range(n)]

print('\n'.join(['Yes' if code == valid else 'No' for code in codes]))
