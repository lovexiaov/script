# coding: utf-8
"""
This tools can show Android forground activity in time.
"""
__author__ = u'lovexiaov'

import os
import re
import time


def start(data):
    pattern = r'^Window\{(.+ )(.+ )(?P<package>.+)/(?P<activity>.+)\}$'

    matches = re.match(pattern, data)
    print(u'============\nPackage: %s\nActivity: %s' % matches.groups()[-2:])


while True:
    # os.system(u"adb shell dumpsys window windows | grep -E 'mCurrentFocus'")
    result = os.popen(u"adb shell dumpsys window windows | grep -E 'mCurrentFocus'").read()
    fields = result.split(u'=')
    if len(fields) != 2: continue

    if fields[1] != u'null':
        try:
            start(fields[1])
        except Exception:
            pass
    time.sleep(1)
