# A program to calculate the area of a circle and the volume of a cylinder using the diameter and height
# 01 May 2021

import math

def circle_area(diameter):
    area = 1/4 * math.pi * math.pow(diameter, 2)   
    return math.floor(area) # added floor during testing .. It was not part of the assignement


def cylinder_volume(diameter, height):
    volume = circle_area(diameter) * height   
    return math.ceil(volume) # added ceil during testing .. It was not part of the assignement


def main():
    diameter = eval(input("Enter diameter:\n"))
    height = eval(input("Enter height:\n"))
    print("The volume of the cylinder is", "{0:.2f}".format(cylinder_volume(diameter, height), 2))
    
    
if __name__=='__main__':
    main()
