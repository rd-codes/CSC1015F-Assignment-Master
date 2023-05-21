# Docstring to test numberutil based on hundreds, tens and units of a number using path coverage
# 16 May 2021

"""
>>> import numberutil
>>> numberutil.aswords(0)      
'zero'
>>> numberutil.aswords(1)      
'one'
>>> numberutil.aswords(22)
'twenty two'
>>> numberutil.aswords(50)
'fifty'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(101)     
'one hundred and one'
>>> numberutil.aswords(130)
'one hundred and thirty'
>>> numberutil.aswords(999)
'nine hundred and ninety nine'

"""
import doctest
doctest.testmod(verbose=True)
