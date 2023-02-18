is_leap_year = False
   
input_year = int(input())

''' Type your code here. '''
if (input_year % 4 == 0)and(input_year % 400 != 100)and(input_year % 400 != 300):
    is_leap_year = True
    
if (is_leap_year):
    print(str(input_year) + " - leap year")
else:
    print(str(input_year) + " - not a leap year")
