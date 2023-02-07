
# IV. Write a program that prompts the user to enter an integer for today's
# day of the week (Sunday is 0, Monday is 1…, and Saturday is 6).
# Also prompt the user to enter the number of days after today for a 
# future day and display the future day of the week. 


from enum import Enum
class days(Enum):
    sunday=0;
    monday=1;
    tuesday=2;
    wednesday=3;
    thrusday=4;
    friday=5;
    saturday=6;
a=int(input("enter toady day of week in 0 to 7 "))
b=int(input("enter no of days after today "))
c=(a+b)%7
print("day after the given number of days is %s"%(days(c).name))