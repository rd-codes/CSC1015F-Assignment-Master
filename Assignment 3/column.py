#A program that asks the user to enter a number, n, where -6<n<2.
#Starting from n, the program will print out every 7th number in the range n to n+41

#Take a number n from user

n = eval(input("Enter a number:\n"))
if n>-6 and n<2:
 for y in range(n,n+41,7):

#An if statement to check if a number should be printed with a width of 2 
  if y>=0 and y<=9:
   print("",y)
  else:
   print(y)
   
  