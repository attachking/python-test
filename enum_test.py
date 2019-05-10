from enum import Enum, unique, IntEnum

e1 = enumerate([1, 2])
print(e1)


def func(cls):
    print(cls)
    return cls


@unique
class VIP(Enum):
    YELLOW = 1
    YELLOW2 = 1
    BLUE = 2
    BLACK = 3


class VIP2(IntEnum):
    YELLOW = 1
    # 不能是str
    # YELLOW = 'str'
    BLUE = 2
    BLACK = 3


print(VIP(2))
try:
    print(VIP(4))
except ValueError as e:
    print(e)
finally:
    pass
print(VIP['YELLOW'])
print(type(VIP.YELLOW) is VIP)
print(VIP.YELLOW.value)
print(VIP.__members__.items())

for index, item in VIP.__members__.items():
    print(index)
    print(item.name)


arr = [1, 2]
for index, item in enumerate(arr):
    print(index, item)
