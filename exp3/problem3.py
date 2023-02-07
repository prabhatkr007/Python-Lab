
# III. Write a program that generates two integers under 100 and 
# prompts the user to enter the sum of these two integers. 
# The program then report true if the answer is correct, false otherwise.


import random
a=random.randint(0,100)
b=random.randrange(0,100,1)
sum=input("enter the sum of integer ")
if(sum==a+b):
    print("answer is true ")
else:
    print("answer is false")
