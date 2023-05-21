#A program that accepts a number, n, where -6<n<2.
#The program will print out the numbers n to n+41 as 6 rows of 7 numbers 
#The first row will contain the values n to n+6
#The second, the values n+7 to n+7+6

#Take a number n from the user input
n = eval(input("Enter the start number:\n"))

#Store your start and stop of your range function and the variable to update your range
start=n
stop=n+7
decre=7
if n>-6 and n <2:
    for x in range(0,6): 
        for y in range(start,stop):
            if y >=0 and y<=9: 
                    print("",y,end=" ")
            else:
                    print(y,end=" ")
#A code to update my range
        start=stop
        stop=stop+decre
        print("")
        
       