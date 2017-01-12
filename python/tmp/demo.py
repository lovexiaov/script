# coding: utf-8
from pprint import pprint

# pprint({u'name':u'lovexiaov', u'age':27, u'color': u'yellow'})
# print({u'name':u'lovexiaov', u'age':27, u'color': u'yellow'})

s = "209,-827,499,-669"

# 1936 1056
t = eval(s)
print(float(t[2] - t[0])/1936,float(t[3] - t[1])/1056)

# for _ in range(2):
#     print(_)