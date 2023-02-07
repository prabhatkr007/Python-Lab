# Write a program to find the sum of all the prime numbers less of equal to a given number. 

def isPrime(n):
     
    if n <= 1 :
        return False
 
    
    for i in range(2, n):
        if n % i == 0:
            return False
 
    return True
 

def sumPrime(n):
    sum=0
    for i in range(2, n ):
        if isPrime(i):
            sum+=i

    return sum      

ans=sumPrime(9)

print("Sum of prime numbers upto 9 is",ans)