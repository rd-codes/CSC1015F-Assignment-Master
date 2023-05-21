# A program that uses recursive functions to find all palindromic primes between two integers N, M
# 03 June 2021

import sys
sys.setrecursionlimit(30000)
from palindrome import isPalindrome
 
# Check if a number is prime
def isPrime(num, divider = 2):
    # Base case
    if num <= 2:
        return True
    if num % divider == 0:
        return False
    if divider * divider > num:
        return True
    # Check if a number is not prime, by dividing it by all the prime numbers less than itself
    return isPrime(num, divider + 1)
   
# Check if a number is a palindromic prime
def isPalindromePrime(n, m):
    # Base case   
    if n > 1 and n <= m:    
        # Use isPrime function to check if a number is prime, and module palindrome to check if a number is palindrome. 
        if isPalindrome(str(n)) and isPrime(n):
            print(n) 
        isPalindromePrime(n + 1, m)
    

def main():
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    isPalindromePrime(N, M)


if __name__ == "__main__":
    main()
    
    