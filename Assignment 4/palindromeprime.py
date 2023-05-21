#A program that finds all palindromic primes between two integers supplied as input (start and end points are excluded)
#10 April 2021
startPoint= eval(input("Enter the start point N:\n"))
endPoint= eval(input("Enter the end point M:\n"))
print("The palindromic primes are:")
for value in range(startPoint+1,endPoint,1):
    for divider in range(2,value):        #Check if a number is prime or not
        if (value % divider ==0): 
            break
    else:
        original=value
        temp= original                      #Temporarly store a number if it's a prime 
        revNum=0
       
        # A code to check if a prime number is a palindrome... Using reversal block 
        while (temp>0):  
            remainder= temp%10
            temp=temp//10
            revNum= revNum*10+remainder
        if(original==revNum):
            print(revNum)       

        
   
   
         
            
            
       