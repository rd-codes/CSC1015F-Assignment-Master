#A program to ask the user to enter a number, n, where -6<n<93.
#The program will print a sequence of 7 numbers, starting from that value
#21 MARCH 2021

#Take a number from the user
n =eval(input("Enter the start number:\n"))

#check if the supplied input lies on our interval
if n>-6 and n<93:
 for x in range(n,n+7,1):
  
#An if block to check if a number should have a space in front 
        if x>=0 and x<=9:
          print("",x,end=" ")
        else:
          print(x,end=" ")

 