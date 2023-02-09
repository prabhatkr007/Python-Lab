# XI. Write a program that displays all possible combinations for picking two numbers from
# integers 1 to 7. Also display the total number of combinations.
# 1    2
# 1    3
# The total number of all combinations is 21.
n = 0
for i in range(1, 8):
    for j in range(1, 8):
        if(i == j):
            continue
        print(i,j)
        n = n + 1
print('The total number of all combinations is :',n)        