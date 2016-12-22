# coding: utf-8
"""
演示环境为 Python 3.5.2，与 Python 2.x 有区别
encode()： 将unicode字符串转换为其他编码字符串，参数为转换后编码
decode()： 将其他编码转换为unicode字符串，参数为转换前编码
"""
__author__ = u'lovexiaov'

s = '中文'
print(type(s), len(s), s) # <class 'str'> 2 中文

u = u'中文'
print(type(u), len(u), u) # <class 'str'> 2 中文

u2s = u'中文'.encode('utf-8')
print(type(u2s), len(u2s), u2s) # <class 'bytes'> 6 b'\xe4\xb8\xad\xe6\x96\x87'

# bytes 2 str
s = str(u2s, encoding=u'utf-8')
print(s) # 中文
# str 2 bytes
b = bytes(u'中文',encoding=u'utf-8')
print(b) # b'\xe4\xb8\xad\xe6\x96\x87'


if __name__ == u'__main__':
    pass