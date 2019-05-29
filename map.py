from functools import reduce

print(max(1, 2, 3, 4))

arr = [1, 2, 3, 4, 5]


def two(x):
    return x * 2


arr1 = map(lambda x: x * 2, arr)
print(arr1)
for index, item in enumerate(arr1):
    print(index, item)

r = reduce(lambda x, y: x + y, arr, 0)
print(r)
