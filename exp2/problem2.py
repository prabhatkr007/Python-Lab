
    # II. The area of a Pentagon can be computed using the following formula(s is the length of a side)
    # Area = (5*s^2)/(4*tan(3.14/5))
    # Write a program that prompts the user to enter the side of a Pentagon and displays   the area.
    
import math 
s = int(input("Enter the side of Pentagon : "))
Area = (5*s*s)/(4*math.tan(3.14/5))

print('The area of a Pentagon : %.2f' %(Area))