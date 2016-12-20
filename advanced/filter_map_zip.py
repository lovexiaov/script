# coding: utf-8
"""
演示 filter、 map 和 zip 的用法:
fileter 将不满足条件的元素过滤掉
map 将元素处理后返回
zip 以两（多）个序列中的最短长度为标准，将这些序列中角标位置相同的元素组合成一个元组（tuple），并返回所有元组的列表
"""

def func(num):
    return True if num > 5 else False

# tuple
# nums = (1, 3, 5, 7, 9)
# set
# nums = {1, 3, 5, 7, 9}
# list
nums = [1, 3, 5, 7, 9]
res = list(filter(func, nums))
print(res)  # [7, 9]

res = list(map(lambda x: x*x, nums))
print(res) # [1, 9, 25, 49, 81]

chars = ['a', 'b', 'c', 'd']
res = list(zip(nums, chars))
print(res) # [(1, 'a'), (3, 'b'), (5, 'c'), (7, 'd')]