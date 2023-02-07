
# II.(Algebra: solve 2*2 linear equations) You can use Cramer's Rule 
# to solve the following 2*2 system of linear equation:ax + by = e  cx + dy = f 
# x =  (ed  -  bf)/(ad - bc) y =  (af  -  ec)/(ad - bc)
# Write a program that prompts the user to enter a, b, c, d, e, and f
# and display the result. If ad - bc is 0, report that the equation has no solution.

a=float(input("enter the value of a : "))
b=float(input("enter the value of b : "))
c=float(input("enter the value of c : "))
d=float(input("enter the value of d : "))
e=float(input("enter the value of e : "))
f=float(input("enter the value of f : "))
if(a*d-b*c==0):
    print("equation has no solution")
else:
    x=(e*d-b*f)/(a*d-b*c)
    y=(a*f-e*c)/(a*d-b*c)
    print("equation has x has value %f and y as value %f"%(x,y))


