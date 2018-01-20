from collections import Iterable, Iterator
from functools import reduce
import os

list1 = list([1, 2, 3, 4, 5])

list1.append(7)
print(list1)
list1.insert(1, 6)
print(list1)
list1.pop(0)
print(list1)

list2 = [x for x in range(0, 100) if x % 2 == 0]  # range函数左闭右开区间
print(list2)


def triangles(n):
    l1 = [1]
    n1 = 1
    yield l1
    while n1 < n:
        l1 = [l1[x] + l1[x - 1] for x in range(n1) if x and x - 1 in range(n1)]
        l1.insert(0, 1)
        l1.append(1)
        yield l1
        n1 = n1 + 1


gen = triangles(10)
print('---generator---')
while True:
    try:
        print(next(gen))
    except StopIteration as e:
        print(e.value)
        break

# iterable  是否可迭代
print(isinstance('asd', Iterable))
print(isinstance([], Iterable))

list3 = [15, 156, 2, 153, 4681961, 1, 16165]


def findminandmax(arr):
    max1 = 0
    min1 = 0
    if isinstance(arr, Iterable):
        for index, item in enumerate(arr):
            if index == 0:
                max1 = item
                min1 = item
            else:
                if item > max1:
                    max1 = item
                if item < min1:
                    min1 = item
        return min1, max1
    else:
        return None, None


print(findminandmax(list3))

list4 = os.listdir('./')
print(list4)

print(isinstance([], Iterator))
# generator
li1 = (x * x for x in range(1, 10))
print(isinstance(li1, Iterator))
for x in [1, 2, 3, 4, 5]:
    print(x)


def test(x1, x2):
    return x1 + x2


print(reduce(test, [1, 2, 3, 4]))
