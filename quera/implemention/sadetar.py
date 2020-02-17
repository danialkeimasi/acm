import sys
import functools

arr = [int(input()) for i in range(4)]
print(
    f'Sum : {sum(arr):.6f}\n'
    f'Average : {sum(arr) / len(arr):.6f}\n'
    f'Product : {functools.reduce(lambda x, y: x * y, arr):.6f}\n'
    f'MAX : {max(arr):.6f}\n'
    f'MIN : {min(arr):.6f}\n'
)
