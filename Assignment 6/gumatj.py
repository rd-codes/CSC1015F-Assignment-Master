# Gumatj Calculations (Conversions between decimals and gumatj numbers)
# 01 May 2021


def gumatj_to_decimal (gumtaj_num):
   
   digit = str(gumtaj_num)
   decimal_num = 0
   pos_digit = 0
   
   # Align each digit with it's power of 5, making sure that the 1st digit gets the highest power and the last digit gets lowest power.
   for exponent in range(len(digit)-1,-1,-1):      
      power = pow(5, int(exponent))
      decimal_num = power*int(digit[pos_digit]) + decimal_num # Sum the product of each digit number with their corresponding powers of 5
      pos_digit += 1
   return decimal_num
      

def decimal_to_gumatj (decimal_num):
   
   gumatj_num = "" 
   if decimal_num != 0:
      # Find the digit corresponding to the lowest power of 5(1st remainder of a decimal_number), and concatenate it with the all the digits of the decimal_number
      while(decimal_num / 5 != 0):
         remainder = decimal_num % 5
         gumatj_num = str(remainder) + gumatj_num 
         decimal_num = decimal_num // 5     
      return gumatj_num     
   else:
      return decimal_num

def gumatj_add (gumatj_num1, gumatj_num2):
   # Convert the two gumatj numbers to decimal numbers, add the two and store the value in answer as a gumatj number.
   decimal1 = gumatj_to_decimal(gumatj_num1) 
   decimal2 = gumatj_to_decimal(gumatj_num2)
   answer = decimal_to_gumatj(decimal1 + decimal2)
   return answer


def gumatj_multiply (gumatj_num1,gumatj_num2):
   # Convert the two gumatj numbers to decimal numbers, multiple the two and store the value in answer as a gumatj number.
   decimal1 = gumatj_to_decimal(gumatj_num1) 
   decimal2 = gumatj_to_decimal(gumatj_num2)   
   answer = decimal_to_gumatj(decimal1 * decimal2 )
   return answer