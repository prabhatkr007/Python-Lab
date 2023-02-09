
# X. A positive integer is called a perfect number if it is equal to the sum of all
# of its positive divisors, excluding itself.  For example, 6 is the first perfect number, 
# because 6 = 3 + 2 + 1 . The next is 28 = 14 + 7 + 4 + 2 + 1. There are four perfect numbers
# less than 10, 000. Write a program to find these four numbers.

for i in range(2, 10001):
    sum_div = 1
    for j in range(2, i):
        if i%j == 0 and j != i:
            sum_div += j
    if sum_div == i:
        print(i)
print("End of program")