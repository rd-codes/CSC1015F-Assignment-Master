"""
>>> import cylinder
>>> cylinder.circle_area(2)
3
>>> cylinder.circle_area(4)
12
>>> cylinder.cylinder_volume(2,5)
16
>>> cylinder.cylinder_volume(1,1)
3

"""
import doctest
doctest.testmod(verbose=True)