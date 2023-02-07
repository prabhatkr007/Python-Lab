
# I. Write a program that prompts the user to enter the length, from the center of Pentagon to a vertex and computes the area of the Pentagon.
    # The formula for computing the area of a Pentagon is:
    # Area = (3*root(3)*s^2)/2
    # where s is the length of a side. The side can be computed using the formula:
    #s = 2*r*sin(3.14/5), where r is the length from the center of a Pentagon to a vertex.

import math
    
length = float(input("Enter the length, from the center of Pentagon to a vertex : "))

s = 2*length*math.sin(3.14/5)

Area = (3*math.sqrt(3)*s*s)/2

print ('Area of Pentagon is %.2f' %(Area))
    