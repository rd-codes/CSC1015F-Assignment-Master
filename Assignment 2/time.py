## A program to check validity of a time entered by the user as a set of three integers
## 26 March 2021

## Input data from the user
#Hours= eval(input("Enter the hours:\n"))
#Minutes= eval(input("Enter the minutes:\n"))
#Seconds=eval(input("Enter the seconds:\n"))

## A loop to check if time given satisfy the range of time
#if Hours >=0:
    #if Hours<=23:
        #if Minutes>=0:
            #if Minutes<=59:
                #if Seconds>=0:
                    #if Seconds<=59:
                        #print("Your time is valid.")
                    #else:
                        #print("Your time is invalid.")
                #else:
                    #print("Your time is invalid.")    
            #else:
                #print("Your time is invalid.")   
        #else:
            #print("Your time is invalid.")
    #else:
        #print("Your time is invalid.")
#else:
    #print("Your time is invalid.")        
    
## The code above is clearly looking horrible
## Refactor it please

def checker(hours,minutes,seconds):
    if (hours >= 0 and hours <= 23) and (minutes,seconds >= 0 and minutes,seconds <= 59):
        print("Your time is valid")
    else:
        print("Your time is invalid")
    return 0;
        
def main():
    hrs = eval(input("Enter the hours:\n"))
    mins = eval(input("Enter the minutes:\n"))
    sec = eval(input("Enter the seconds:\n"))    
    checker(hrs,mins,sec)
    
    
if __name__ == "__main__":
    main()
    
#Très bien, merci beaucoup
    
