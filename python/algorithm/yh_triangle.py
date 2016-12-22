# coding: utf-8
"""
This is module docs.
"""
__author__ = 'lovexiaov'

def yh_triangle(columns):
    """
    前提：每行端点与结尾的数为1.
    每个数等于它上方两数之和。
    每行数字左右对称，由1开始逐渐变大。
    第n行的数字有n项。
    第n行数字和为2n-1。
    ...
              1
            1   1
          1   2   1
        1   3   3   1
      1   4   6   4   1
    1   5   10  10  5   1
    """
    b = [1]
    n = 0
    while n < columns:
        yield b
        b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
        n += 1

if __name__ == u'__main__':
    for line in yh_triangle(6):
        print line