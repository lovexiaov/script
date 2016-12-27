# coding: utf-8
"""
globals() return a dict of current scope's global variables.
locals() return a dict of current scope's local variables.
"""
__author__ = u'lovexiaov'

from pprint import pprint

s = u'hello world'

pprint(globals())
'''
{'__author__': 'lovexiaov',
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': '\n'
            "globals() return a dict of current scope's global variables.\n"
            "locals() return a dict of current scope's local variables.\n",
 '__file__': 'd:/weixy/code/script/python/advanced/globals_locals.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000000009D5E10>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'func': <function func at 0x00000000001C7F28>,
 'pprint': <function pprint at 0x0000000000DA7E18>,
 's': 'hello world'}
'''

pprint(locals()) # 同上


def func():
    s = u'lovexiaov'
    pprint(globals())
    '''
    {'__author__': 'lovexiaov',
     '__builtins__': <module 'builtins' (built-in)>,
     '__cached__': None,
     '__doc__': '\n'
                "globals() return a dict of current scope's global variables.\n"
                "locals() return a dict of current scope's local variables.\n",
     '__file__': 'd:/weixy/code/script/python/advanced/globals_locals.py',
     '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000000009C5E10>,
     '__name__': '__main__',
     '__package__': None,
     '__spec__': None,
     'func': <function func at 0x0000000000927F28>,
     'pprint': <function pprint at 0x0000000000A97E18>,
     's': 'hello world'}
    '''
    pprint(locals()) #{'s': 'lovexiaov'}



if __name__ == u'__main__':
    func()