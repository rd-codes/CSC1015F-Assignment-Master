#A program that ask the user for a month name and start day and then prints the calendar for that month in a 6 row by 7 column grid(Assuming February has 28 days).
# 10 April 2021

month = input("Enter the month ('January', ..., 'December'):\n")
day = input("Enter the start day ('Monday', ..., 'Sunday'):\n")
LastDay=31
Number_Of_Days_In_A_Week=7
# A loop to set the end day of the week depending on the start day.
if (day=="Monday"):
    StartDay=1
    StopDay=Number_Of_Days_In_A_Week
if (day=="Tuesday"):
    StartDay=0 
    StopDay=Number_Of_Days_In_A_Week-1
elif (day=="Wednesday"):
    StartDay=-1
    StopDay=Number_Of_Days_In_A_Week-2
elif (day=="Thursday"):
    StartDay=-2
    StopDay=Number_Of_Days_In_A_Week-3
elif (day=="Friday"):
    StartDay=-3
    StopDay= Number_Of_Days_In_A_Week-4
elif(day=="Saturday"):
    StartDay=-4
    StopDay=Number_Of_Days_In_A_Week-5
elif(day=="Sunday"):
    StartDay=-5  
    StopDay=Number_Of_Days_In_A_Week-6
#Check if the given month and day are valid
if (month=="January"or month=="February" or month=="March" or month=="April" or month=="May" or month=="June" or month== "July" or month=="August" or month=="September" or month =="October" or month =="November" or month=="December"):
    if (day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday" or day=="Saturday" or day=="Sunday"):
        print(month)
        print("Mo","Tu","We","Th","Fr","Sa","Su")
    
    for week in range(1,8):    
# Ensure that the number of days doesn't go beyond 31 and it is the correct one for each month
            if StopDay>LastDay: 
                if (month=="February"):
                    StopDay=28
                elif (month=="April"or month=="June"or month=="September" or month=="November"):
                    StopDay=30
                else:
                    StopDay=31     
            for date in range(StartDay,StopDay+1):
 # Make the field width to be two and print spaces if Start day< 0 or greater than 31
                    if date<=0:
                        print("  ",end=" ")
                    elif date>=1 and date <=9: 
                        print("",date,end=" ")
                    else:
                        print(date,end=" ")
# Update the end day of a week, depending on what the start day was
            StartDay= StopDay +1
            StopDay= StopDay + Number_Of_Days_In_A_Week
            print("")
                        
        
