from itertools import combinations
import itertools
import math
import time


def pascal(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    numbers = [1, 1]
    for i in range(n-2):
        numbers = [1] + [numbers[i] + numbers[i+1] for i in range(len(numbers) - 1)] + [1]

    return numbers


def pascal_rect_1(n):
        return '\n'.join(map(str, [pascal(i) for i in range(1, n + 1)]))


start_time = time.time()
pascal_rect_1(400)
print("--- %s seconds ---" % (time.time() - start_time))


##############################
##############################


def pascal_gen():
    yield [1]
    yield [1, 1]

    numbers = [1, 1]
    for i in itertools.count(2):
        numbers = [1] + [numbers[i] + numbers[i+1] for i in range(len(numbers) - 1)] + [1]
        yield numbers


def pascal_rect_2(n):
    gen = pascal_gen()
    rows = [' '.join(map(str, next(gen))) for i in range(1, n + 1)]
    return '\n'.join(rows)


start_time = time.time()
pascal_rect_2(400)
print("--- %s seconds ---" % (time.time() - start_time))
