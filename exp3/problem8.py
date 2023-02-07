# Write a program that reads three edges for a triangle and 
# computes the perimeter if the input is valid. Otherwise,display 
# that the input is invalid. The input is valid if the sum of 
#  every pair of two edges is greater than the remaining edge. 


edge1 = float(input("Enter the edge 1 of triangle :"))
edge2 = float(input("Enter the edge 1 of triangle :"))
edge3 = float(input("Enter the edge 1 of triangle :"))

if( (edge1 + edge2)  > edge3):
    if(edge1 + edge3 > edge2):
        if(edge2 + edge3 > edge1):
            print("Valid value .")
            print("Perimeter is %.2f:"%(edge1+edge2+edge3) )
else:
    print("Not a Triangle , Invalid Value;")