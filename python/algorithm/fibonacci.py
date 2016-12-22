# coding: utf-8
"""
This is module docs.
"""
__author__ = 'lovexiaov'
def fibonacci(length):
    """
    指的是这样一个数列：1、1、2、3、5、8、13、21、34。
    在数学上，斐波纳契数列被以递归的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>2，n∈N*）
    """
    n, a, b = 0, 0, 1
    while n < length:
        yield b
        a, b = b, a + b
        n += 1
    print('done')

if __name__ == u'__main__':
    for i in fibonacci(5):
        print(i)