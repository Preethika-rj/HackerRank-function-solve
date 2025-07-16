from functools import reduce

n, m = map(int, input().split())
array = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(reduce(
    lambda x, y: (x + 1) if y in a else x - 1 if y in b else x,
    array,
    0
    ))
