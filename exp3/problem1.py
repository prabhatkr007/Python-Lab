
# I. (Algebra: solve quadratic equations) The two roots of a quadratic equation, 
# for example, a + bx +c = 0, can be obtained using the following formula:
# r1 = (-b + )/2a       and          r2 = (-b - )/2a       
# b2-4ac is called the discriminant of the quadratic equation. If it is positive, 
# the equation has two real roots. If it is zero, the equation has one root. If it is negative,
# the equation has no real roots.Write a program that prompts the user to enter values for a,b, and c
# and displays the result based on the discriminant. If the discriminant is positive, display two roots.
# If discriminant is 0, display one root. Otherwise display the equation has no real roots. 


import math
a= float(input("enter the value of a :"))
b= float(input("enter the value of b : "))
c= float(input("enter the value of c : "))
if((math.pow(b,2)-4*a*c)>0):
   r1=(-b+math.sqrt(math.pow(b,2)-4*a*c))/2*a
   r2=(-b+math.sqrt(math.pow(b,2)+4*a*c))/2*a
   print("roots are %f and %f"%(r1,r2))
elif((math.pow(b,2)-4*a*c)==0):
    r1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 * a
    print(" system has single root as %f"%r1)
else:
    print("System has no real roots")
