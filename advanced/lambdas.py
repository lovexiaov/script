# coding: utf-8
__author__ = 'lovexiaov'
"""
Python 中，lambda 表达式只能包含一条语句（这条语句将作为该表达式的返回值）。所以，语句中不能使用 return, print 等关键词
"""
def adv(func, var):
    func(var)
    

adv(lambda x: str(x), 'hello')