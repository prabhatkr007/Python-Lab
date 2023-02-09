    
# V.  Use nested loop that display the following patterns in  four separated programs:

print('Pattern A')

for x in range(6,0,-1):
    for y in range(1,x+1):
        print(y,end=" ")
    print()   

print('Pattern C')

for i in range(1,7):
    num = 1
    for j in range(7, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")


