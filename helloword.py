#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('hello word')
if not True:
    print('not')
else:
    print('222')
print('%03d' % 2)
print('%.2f' % 2.165151)
print('%f %d %s %x %%' % (2.165151, 2, '123', 0x12))
# 获取字符整数表示
print(ord('陈'))
# 获取整数字符表示
print(chr(60))
# 10进制转16进制
sj = ''
sjList = [30003, 23567, 30002, 25105, 29233, 20320]
for i, n in enumerate(sjList):
    sj += chr(n)
# print(sj)
print(str('\\u' + hex(ord('陈'))[2:]))


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
del list2[0:2]  # 左闭右开区间
print(list1)
print(list2)

map1 = {
    'name': '陈'
}
print(map1)
print(map1['name'])
print(map1.get('na'))  # 用get方法如果键值对不存在则返回None, 如果不用get则会报错
print(map1.get('name'))

if map1.get('name') is not None:
    print('---test---')

str1 = input('请输入：')
print(type(str1))
for x in range(1, 3):  # 左闭右开区间
    print(x)
