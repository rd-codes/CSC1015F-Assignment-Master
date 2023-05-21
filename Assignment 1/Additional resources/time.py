# Program to convert an amount of minutes into an equivalent amount 
# of days, hours and minutes.
#
# Name: Stephan Jamieson
#
minutes = int(input_str)
days = hours//24

print(".")

hours = minutes//60

print("The number of days is", days, end=', ')
print("and the number of minutes is", minutes, end='')

minutes = minutes%60

print("the number hours is", hours, end=', ')

input_str = input("Enter a quantity of minutes: ")
hours = hours%24