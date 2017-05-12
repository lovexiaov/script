# coding: utf-8
"""
This module show you how to interact with time module.

%a Abbreviated weekday name
%A Full weekday name
%b Abbreviated month name
%B Full month name
%c Date and time representation appropriate for locale
%d Day of month as decimal number (01 - 31)
%H Hour in 24-hour format (00 - 23)
%I Hour in 12-hour format (01 - 12)
%j Day of year as decimal number (001 - 366)
%m Month as decimal number (01 - 12)
%M Minute as decimal number (00 - 59)
%p Current locale's A.M./P.M. indicator for 12-hour clock
%S Second as decimal number (00 - 59)
%U Week of year as decimal number, with Sunday as first day of week (00 - 51)
%w Weekday as decimal number (0 - 6; Sunday is 0)
%W Week of year as decimal number, with Monday as first day of week (00 - 51)
%x Date representation for current locale
%X Time representation for current locale
%y Year without century, as decimal number (00 - 99)
%Y Year with century, as decimal number
%z, %Z Time-zone name or abbreviation; no characters if time zone is unknown
%% Percent sign
"""
__author__ = u'lovexiaov'

import time
import datetime
def format():
    print(datetime.datetime.now()) # 2017-05-12 18:36:19.921000
    print(datetime.datetime.now().strftime(u'%b-%d-%Y %H:%M')) # May-12-2017 18:36
    print(time.strftime(u'%b-%d-%Y %H:%M')) # May-12-2017 18:36
    print(time.strftime(u'%Y-%m-%d-%H-%M-%S')) # May-12-2017 18:36
if __name__ == '__main__':
    format()
