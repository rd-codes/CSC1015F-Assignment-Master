# A docstring for  cases that achieve tests for statement coverage
# 17 May 2021

"""
>>> import timeutil
>>> timeutil.validate("12:59 a.m.")
True
>>> timeutil.validate("01:21 a.m.")
False
>>> timeutil.validate("9at:04 a.m.")
False
>>> timeutil.validate("9:9at a.m.")
False
>>> timeutil.validate(" 22:50 a.d.")
False
>>> timeutil.validate(":10 p.m.")
False

"""
import doctest
doctest.testmod(verbose=True)
