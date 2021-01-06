"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

# datetime is useful to get the current time stamp
# sys.argv: anything you pass in after the file name, when you run the file it can take it in as an argument (information that you want)
# take in arguments from the command line using sys.argv
# study documentation on calendar and datetime
# command line arguments are returned as strings

import sys
import calendar
from datetime import datetime

date = datetime.now() # gets todays date
current_month = date.month # accessing current month through the stored date variable
current_year = date.year # accessing current year through the stored date variable 
if len(sys.argv) == 1:
  month = current_month # assigning month and year to current_month and current_year
  year = current_year
elif len(sys.argv) == 2:
  month = int(sys.argv[1]) # position 0 is the file name & arguments start after that
  year = current_year
else:
  month = int(sys.argv[1])
  year = int(sys.argv[2])

cal = calendar.TextCalendar().formatmonth(year, month) # "prmonth" shows "None" in terminal
print(cal)

# DOC'S CODE -->

# import sys
# import calendar
# from datetime import datetime
# # $%$Start
# l = len(sys.argv)
# if l == 1:
#     # User didn't specify any input
#     month = datetime.now().month
#     year = datetime.now().year
# elif l == 2:
#     # User didn't specify year
#     month = int(sys.argv[1])
#     year = datetime.now().year
# elif l == 3:
#     # User specified both month and year
#     month = int(sys.argv[1])
#     year = int(sys.argv[2])
# else:
#     # User provided faulty input
#     print("usage: calendar.py [month] [year]")
#     sys.exit(1)
# cal = calendar.TextCalendar()
# cal.prmonth(year, month)


# JOANNE'S CODE -->

# import sys
# import calendar as cal
# from datetime import datetime as dt
# # Create variable to hold today's date
# today = dt.today()
# # Get the user's input from the command line and check edge cases
# # If user enters all required inputs in the command line
# if len(sys.argv) == 3:
#     # Convert user input to ints and return the calender month and year
#     print(cal.TextCalendar().formatmonth(int(sys.argv[2]), int(sys.argv[1])))
#     sys.exit(0)  # Exits the program
# # If the user only enters one argument, such as month but not year or vise versa
# elif len(sys.argv) == 2:
#     # Return current in place of missing value from user input
#     if int(sys.argv[1]) in range(12):
#         print(cal.TextCalendar().formatmonth(today.year, int(sys.argv[1])))
#         sys.exit(0)  # Exits the program
#     elif int(sys.argv[1]) in range(1000, 2021):
#         print('Year', int(sys.argv[1]))
#         print(cal.TextCalendar().formatmonth(int(sys.argv[1]), today.month))
#         sys.exit(0)  # Exits the program
# # If the user does not enter and arguments in the command line
# if len(sys.argv) == 1:
#     # Return current month and year
#     print(cal.TextCalendar().formatmonth(today.year, today.month))
#     sys.exit(0)  # Exits the program
# # If user enters an invalid format
# else:
#     print('Usage: 14_cal.py [month number] [year]')  # Return usage statement
#     sys.exit(1)  # Exit the program