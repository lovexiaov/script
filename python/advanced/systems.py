# coding: utf-8
"""
This module show you how the python interact with the system.
"""
__author__ = u'lovexiaov'

import os
import sys

# run system command
os.system(u'echo "hello world." >> hi.txt')

# add specific path to current envireonment path

sys.path.append(os.path.join(os.getcwd(), r'../common'))
print(sys.path)
import common.objects

try:
    # import module use exec
    exec(u'import systems as syss')
except ImportError as err: # if the module does not exists.
    print(err)
if __name__ == u'__main__':
    print(syss.__doc__)
    