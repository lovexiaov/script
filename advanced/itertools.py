# coding: utf-8
__author__ = 'lovexiaov'
"""
'accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle', 'dropwhile', 'filterfalse', 'groupby', 'islice', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee', 'zip_longest'
"""

from itertools import *
from time import sleep

nums = (1, 2, 3, 4, 5)
s = u'hello'
a = [u'A', u'B']


# accumulate(iterable[, func]) --> accumulate object
# |-- 将可迭代对象中的元素依次相加，并返回
# result = list(accumulate(nums))
# print(result)  # [1, 3, 6, 10, 15]
# result = list(accumulate(s))
# print(result)  # ['h', 'he', 'hel', 'hell', 'hello']

# chain(*iterables) --> chain object
# |-- 将所有参数依次迭代后返回
# result = list(chain(s, nums, a))
# print(result)  # ['h', 'e', 'l', 'l', 'o', 1, 2, 3, 4, 5, 'A', 'B']

# combinations(iterable, r) --> combinations object
# |-- 以 r 为长度，返回可迭代对象元素的所有有序组合
# result = list(combinations((1, 2, 3), 2))
# print(result)  # [(1, 2), (1, 3), (2, 3)]
# result = list(combinations((3, 2, 1), 2))
# print(result)  # [(3, 2), (3, 1), (2, 1)]

# combinations_with_replacement(iterable, r) --> combinations_with_replacement object
# |-- 以 r 为长度，返回可迭代对象元素的所有有序组合（允许同一个元素重复出现）
# result = list(combinations_with_replacement((1, 2, 3), 2))
# print(result)  # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

# compress(data, selectors) --> iterator over selected data
# |-- 根据 selectors 对应位置元素的值来过滤 data 中的元素
# result = list(compress(u'ABCDEFG', ('a', 0, None, 1, True, False)))
# print(result)  # ['A', 'D', 'E']

# count(start=0, step=1) --> count object
# |-- 从 start 开始，以 step 为步频的无限计数器
# for i in count(3, 1):
#     if i > 10: break
#     print(i)

# cycle(iterable) --> cycle object
# |-- 对一个可迭代对象无限循环迭代
# for i in cycle(nums):
#     print(i)
#     sleep(2)

# dropwhile(predicate, iterable) --> dropwhile object
# |-- 如果 predicate 为 True， 则丢弃相应元素；否则将剩余对象作为 generator 返回
# for i in dropwhile(lambda x: x < 3, nums):
#     print(i)  # 3 4 5
# result = list(dropwhile(lambda x: x < 3, nums))
# print(result)  # [3, 4, 5]

# filterfalse(function or None, sequence) --> filterfalse object
# |-- 如果 function 返回 True，则过滤相应元素；如果 function 为 None，则过滤所有元素
# result = list(filterfalse(lambda x : x > 3, nums))
# print(result)
# result = list(filterfalse(None, nums))
# print(result)

# groupby(iterable[, keyfunc]) -> create an iterator which returns (key, sub-iterator) grouped by each value of key(value).
# |-- 创建迭代器，以某种规则（keyfunc）将可迭代对象分组，然后返回(keyfunc 返回值, 分组结果迭代器)
# lst = ['aa', 'bc', 'cbd', 'eefd', 'e']
# result = groupby(lst, len)
# for i,k in result:
#     print(u'{0} : {1}'.format(i, list(k)))
#     # print result:
#     # 2 : ['aa', 'bc']
#     # 3 : ['cbd']
#     # 4 : ['eefd']
#     # 1 : ['e']

# product
# result = list(product(a, range(3)))
# print(result)

