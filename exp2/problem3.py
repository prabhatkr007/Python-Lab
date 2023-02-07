
# III. (Reverse number) Write a program that prompts the user to enter a four-digit integer 
# and display the number in reverse order. 

num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num//10

print("Reversed Number: %i" %(reversed_num))