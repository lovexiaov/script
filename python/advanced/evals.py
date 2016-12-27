# coding: utf-8
"""
This module demonstrate the use of buildin function eval().
"""
__author__ = u'lovexiaov'

s = '0, 1, 2, 3'
print(eval(s))  # (0, 1, 2, 3)
s = '3 * 5'
print(eval(s))  # 15
s = '1 + 2 *  3  / 4'
print(eval(s))  # 2.5
s = '1 2 3'
# print(eval(s))  # SyntaxError: invalid syntax

if __name__ == u'__main__':
    pass
