# V. Suppose you shop for rice and find it i two different sized packets. 
# You would like to write a program to compare the costs of the packages. 
# The program prompts the user to enter the weight and price of each package
# and the displays the one with the better price. 

package1= eval(input("Enter cost of Package1 please: "))
package2= eval(input("Enter cost of Package2 please: "))
if package1 < package2:
    print("Package2 is the better option")
if package2 < package1:
    print("Package1 is the better option")
if package2 == package1:
        print("No difference between the two packages")