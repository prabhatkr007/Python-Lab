#  Write a program that prompts the user to enter an integer and 
#  check whether the number is divisible by both 5 and 6,divisible 
#  by 5 or 6 or just one of them (but not both of them).

number = int(input("Enter the integer : "))

if((number%5 == 0) & (number%6 == 0)):
    print("Divisible by 5 & 6")

if(number%5 == 0):
    print("Divisible by 5")

if(number%6 == 0):
    print("Divisible by 6")

if((number%5 != 0) & (number%6 != 0)):
    print("Not Divisible by 5 & 6")
