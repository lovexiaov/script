# coding: utf-8
"""
This module demonstrate how to encode and decode urls.
"""
from pprint import pprint

__author__ = u'lovexiaov'

from urllib import urlencode, quote, unquote
from urlparse import urljoin

data = {
    'name': '张三',
    'age': 24
}
city = '丰台'

# 键值对通过 urlencode 编码
print(urlencode(data))  # age=24&name=%E5%BC%A0%E4%B8%89
# 单个字符串通过 quote 编码
print(quote(city))  # %E4%B8%B0%E5%8F%B0

# 通过 unquote 解码，注意：没有 urldecode 方法
print(unquote('age=24&name=%E5%BC%A0%E4%B8%89'))  # age=24&name=张三
print(unquote('%E4%B8%B0%E5%8F%B0'))  # 丰台

pprint(urljoin('http://lovexiaov.cn/', 'weather.html'))
pprint(urljoin('http://lovexiaov.cn', 'weather.html'))


