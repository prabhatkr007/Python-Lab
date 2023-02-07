    # II. Write a program that reads the radius and length of a cylinder, 
    # to compute the area and volume of the cylinder.

radius = float(input("Enter the radius : "))
length = float(input("Enter the length : "))

area = 3.14*radius*radius
volume = area*length

print("area of cylinder : %.2f and Volume of cyinder : %.2f" %(area, volume) )
