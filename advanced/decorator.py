# coding: utf-8
import time
from functools import wraps
import datetime

def showTime(func):

    # @wraps(func) # no need to use it
    def wrapper():
        print(datetime.datetime.now())
        func() # style 1
        # return func() # style 2
    return wrapper

@showTime
def sayHi():
    time.sleep(2)
    print("Hello!")

sayHi()