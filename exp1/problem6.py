# Write a program that calculates the distance between two points, 
# where the coordinates of the points are provided by the user.
import math

x1= float(input("enter the x1: "))
y1 = float(input("enter the y1: "))
z1 = float(input("enter the z1: "))

x2= float(input("enter the x2: "))
y2 = float(input("enter the y2: "))
z2 = float(input("enter the z2: "))

ans = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2))

print("Distance between given coordinates is : %.2f" %(ans))