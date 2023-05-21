from math import sqrt
#A program to approximate PI and then computes and the area of a circle with radius entered by the user.
#10 April 2021

#Store the values that are repeating themselves in the formula for approximating pi and initialise values for updating our next factor/nextTerm
firstTerm=2
numar = firstTerm
denom = sqrt(2)
nextTerm =0
pi = firstTerm
# A loop to estimate pi
while nextTerm!=1:
    nextTerm = numar/denom
    pi= pi*nextTerm
    denom = sqrt(2+denom) # Update denominator
print("Approximation of pi:",round(pi,3))
radius= eval(input("Enter the radius:\n"))
area= pi*radius**2  # Formula for area of circle
print("Area:",round(area,3))