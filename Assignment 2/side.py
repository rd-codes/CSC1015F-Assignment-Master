from math import *
# A program to calculate a side of a right-angle triangle
# 26 March 2021
 
# Input the two known side from the user
a= eval(input("Enter the length of side a:\n"))
c= eval(input("Enter the length of side c:\n"))

if a >0:
    if c>0:
        b = sqrt((c*c)-(a*a)) # formula for calculating b
        print("The length of side b is",b,end='.')
    else:
        print("Sorry, lengths must be positive numbers.")
else:
    print("Sorry, lengths must be positive numbers.")        
            

