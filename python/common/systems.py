# coding: utf-8
"""
This module show you how the python interact with the system.
"""
__author__ = u'lovexiaov'

import os
import sys
import platform

# 获取当前 python 版本信息
print(sys.version_info) # sys.version_info(major=3, minor=5, micro=2, releaselevel='final', serial=0)

# 获取当前环境变量
# print(os.environ)
# 获取运行平台的架构信息
print(platform.architecture()) # ('64bit', 'WindowsPE')
# 获取运行平台的版本
print(platform.version()) # 6.1.7601

# run system command
os.system(u'echo "hello world." >> hi.txt')

# add specific path to current envireonment path

sys.path.append(os.path.join(os.getcwd(), r'../advanced'))
print(sys.path)
import advanced.evals

try:
    # import module use exec
    exec (u'import systems as syss')
except ImportError as err:  # if the module does not exists.
    print(err)
if __name__ == u'__main__':
    print(syss.__doc__)

