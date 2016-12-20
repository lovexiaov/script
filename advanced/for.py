# coding: utf-8
"""
This is module docs.
"""
__author__ = u'lovexiaov'

# 标准 for 循环（单因子 for 循环），遍历序列
for i in (u'hello', u'world'):
    print(i)
    """
    output:
    hello
    world
    """

for c in u'hello':
    print(c)
    """
    output:
    h
    e
    l
    l
    o
    """

# 变形 for 循环（多因子 for 循环），遍历序列中的子元素
# 要求：子元素必须是可迭代对象（str, dict, set, list, tuple, etc.)，且长度等于因子个数
for i, j, k in (u'hel', u'wor'):
    print(i + u'--' + j + u'--' + k)
    """
    output:
    h--e--l
    w--o--r
    """

for i, j, k in (u'he',):
    print(i + j) # ValueError: need more than 2 values to unpack

if __name__ == u'__main__':
    pass