#A program to ask the user to enter a number, n, where -6<n<93.
#The program will print a sequence of 7 numbers, starting from that value
#MNTALL003
#21 MARCH 2021

#Take a number from the user
n =eval(input("Enter the start number:\n"))

#check if the supplied input lies on our interval
if n>-6 and n<93:

#A loop that will run 7 times to print out a sequence of seven numbers
 for x in (0,7):
  if n>=0 and n<=9:
              print("",n,end="")
  else:
   print(n,end="")
   
  
 