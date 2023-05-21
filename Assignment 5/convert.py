# A program to transform a date and time given in a compact 24-hr to a long form 12-hour format
# 16 April 2021

date_time = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

time=0
month_name = "January,February,March,April,May,June,July,August,September,October,November,December".split(",")
time_suffix = "am,pm".split(",")
day_suffix = "st,nd,rd,th".split(",")
# Split the date and time given into its components
year = date_time[0:4]
month_number = date_time[5:7]
day = date_time[8:10]
time_in_hours = date_time[11:13]
time_in_minutes= date_time[14:16]
# Check the formart suitable for year by checking the last two digits of year
if year[2:5]=="00":
    year="'00"
else:
    year="'"+year[2:5]
# Remove the zero in front of the month number   
if int(month_number)>=1 and int(month_number)<10: 
        month_number= month_number[1:2]                   
# Change the month number to a month name
month_number = int(month_number)
month_number = month_name[month_number-1]
# Check whether it's after/mid-night and before mid-day
time_in_hours= int(time_in_hours)
if time_in_hours>=0 and time_in_hours<12:
    if int(time_in_hours) ==0:
        time_in_hours= "12"
    time_suffix= time_suffix[0]
else:
# Check whether it's after/mid-day and before mid-night
    time_suffix = time_suffix[1]
    if time_in_hours> 12: 
            time_in_hours = time_in_hours-12       
    else:
        time_in_hours=str(time_in_hours)
time= str(time_in_hours) +":"+ time_in_minutes # Convert time to a long form "12-hour format"
# Remove the zeros in front of the day number
if int(day)>=1 and int(day)<10: 
    day= day[1:2]       
# Ensure each day number has a suitable suffix
if int(day)==1 or int(day)==21 or int(day)==31:
    day =str(day)+day_suffix[0]
elif int(day)==2 or int(day)==22:
    day= str(day)+day_suffix[1]
elif int(day)==3 or int(day)==23:
    day= str(day)+day_suffix[2]
else:
    day= str(day)+day_suffix[3]

print(time,time_suffix,"on the",day,"of",month_number,year)