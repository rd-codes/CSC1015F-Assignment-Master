# A program to take a data from user and formart it
# 26 March 2021

# Assign user inputs data to relevant variables
Runner_Name = input("Enter runner's name:\n")
Day_Of_Month= input("Enter day of month:\n")
Month_Of_Year= input("Enter month of year:\n")
Year= input("Enter year:\n")
Completion_Time= eval(input("Enter completion time (in mins):\n"))
Prize_Money =input("Enter prize money (in rand):\n")
print("")
Marathon= float(42.195)
Average_Distance= Completion_Time/Marathon
print(Runner_Name,"completed the race on",end=' ')
print(Day_Of_Month,Month_Of_Year,Year,sep='/',end=' ')
print("in",Completion_Time,"minutes",end='.\n')
print("The runner wins R",Prize_Money,end='.',sep='')
print("")
print("Average time per kilometer was",Average_Distance,"minutes.")
