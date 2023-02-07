
# VI. (Find the number of days in a month) Write a program that prompts the user to enter the month and
# year and displays the number of days in the month. For example, if the user entered month 2 and year 2000, 
# the program should display that February 2000 has 29 days. If the user entered 3 and year 2005, the program 
# should display that March 2005 has 31 days.

month=int(input("enter month"))
yr=int(input("enter year"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print(" days are 31")
elif month==2:
    
    if(yr%100 == 0):
        if(yr%400 == 0):
            print("days are 29.");
        else:
            print("days are 28");
    elif(yr%100 != 0 and yr%4 ==0):
        print("days are 29");
    else:
        print("days are 28")
else:
    print("days are 30")



