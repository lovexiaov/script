# coding: utf-8
"""
This module shows you how to use regex expression with python.
"""
__author__ = u'lovexiaov'

import re


def group_reference():
    # `\1` 表示引用 group 1（group 索引是从 1 开始的，0 代表最大匹配项）
    pattern = r"(.+)(\d*) \1+"

    match = re.match(pattern, 'abc123 abcabcddd')
    if match:
        print(u'match 1')
        print(match.groups())  # ('abc', '123')
        print(match.group(0))  # abc123 abcabc
        print(match.group(1))  # abc
        print(match.group(2))  # 123

    match = re.match(pattern, u'abc abd')
    if match:
        print(u'match 2')

    match = re.match(pattern, u'!@# !@#===')
    if match:
        print(u'match 3')
        print(match.groups())  # ('!@#', '')
        print(match.group(0))  # !@# !@#
        print(match.group(1))  # !@#
        # print(match.group(2)) # empty string


if __name__ == u'__main__':
    # group_reference()
    t = u'Window{428ba540 u0 com.unicom.gudong.client/com.gudong.client.MainActivity}'

    pattern = r'^Window\{(.+ )(.+ )(.+)/(.+)\}$'
    match = re.match(pattern, t)
    print(match.groups())
