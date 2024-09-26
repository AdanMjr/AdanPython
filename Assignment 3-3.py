# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31
# I used allowed the interactive input with float(input())
year = float(input())
month = float(input())
day = float(input())

# Get the year, then the month, then the day
# housekeeping()

# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
# to make sure the users date was shown I used print(int)
if validDate == True: print(int(month),"/",int(day),"/",int(year),"is a valid date.")
    # Output statement
else: print(int(month),"/",int(day),"/",int(year),"is an invalid date.")
    # Output statement