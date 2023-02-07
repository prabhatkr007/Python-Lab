# VII. Write a program that calculates the energy needed to heat the water 
# from an initial temperature to a final temperature. Program prompts the user 
# to provide the amount of waters in kilograms and the initial and final temperatures of water. 
   
water = float(input("Enter amount of water in KG :"))
inital = float(input("Enter the intial temperature : "))
final = float(input("Enter the final temperature : "))

energy =  water*(final - inital)*4184

print("%.2f Joule energy needed to heat the water"%(energy))