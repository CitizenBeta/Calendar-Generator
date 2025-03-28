# File Name: calendar_generator.py
# Author: Zhang Anjun
# Date: 2025-03-14
# Description: Calendar generator
# Version: 1.4
# © 2025 Zhang Anjun. All rights reserved.
from sys import exit

# Copyright notice
def copyrightNotice():
    print("")
    print("Author: Zhang Anjun")
    print("Version: 1.4")
    print("© 2025 Zhang Anjun. All rights reserved.")
    print("")

# Shared functions
def leap(y):
    # Leap year is divisible by 4 but not by 100 or it is divisible by 400
    return (((y%4 == 0) and (y%100 != 0)) or (y%400 == 0))
    
def maxDays(m, y):
    # Months with 31 days
    if ((m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12)):
        return 31
    # Months with 30 days
    elif ((m == 4) or (m == 6) or (m == 9) or (m == 11)):
        return 30
    # February has 29 days if leap year, otherwise 28 days
    elif (m == 2):
        if leap(y):
            return 29
        else:
            return 28

# Calculate the number of days from 1900
def daysInFullYearsBefore(y):
    total = 0
    i = 1900
    while i != y:
        if leap(i):
            total = total + 366
        else:
            total = total + 365
        i = i + 1
    return total

# Calculate the number of days from January
def daysInFullMonthsBefore(m, y):
    total = 0
    i = 1
    while i != m:
        total = total + maxDays(i, y)
        i = i + 1
    return total

# Calculate the total number of days from 1-1-1900
def daysSince1900(d, m, y):
    return daysInFullYearsBefore(y) + daysInFullMonthsBefore(m, y) + d

# Calendar Generator
# "prompt()" function is called by the end of the program
def prompt():
    m = int(input("Enter a month (1-12): "))
    # Verify month input
    if m < 1 or m > 12:
        print("Invalid month.")
        exit(0)
    
    # Verify year input
    y = int(input("Enter a year (after 1900): "))
    if y < 1900:
        print("Invalid year.")
        exit(0)
    
    print("")
    # Display the title with the month and year
    print("Calendar for ", m, "-", y, sep="")
    calendar(m, y)

def printWeek(weekday):
    # Print weekday name according to the "weekday" index
    # Note that Monday is "1" instead of "0"
    if weekday == 1:
        print("Mon ", end="")
    elif weekday == 2:
        print("Tue ", end="")
    elif weekday == 3:
        print("Wed ", end="")
    elif weekday == 4:
        print("Thu ", end="")
    elif weekday == 5:
        print("Fri ", end="")
    elif weekday == 6:
        print("Sat ", end="")
    elif weekday == 7:
        print("Sun ", end="")

def printDate(d):
    if d >= 10:
        # Two-digit numbers print two spaces
        print("  ", d, " ", end="", sep="")
    elif d < 10 and d > 0:
        # Single-digit numbers print one extra space (i.e. 3)
        print("   ", d, " ", end="", sep="")
    elif d <= 0:
        # Zero or negative dates mean that these are only placeholders
        print("     ", end="", sep="")
    # Note that using parameters "end" and "sep"
    # is to print the date within a row
    
def printRow(weekday, d, m, y):
    # Print the header for the row
    printWeek(weekday)

    # Adjust the starting date based on the current weekday column
    d = d + weekday

    # Run through the whole month
    while d <= maxDays(m, y):
        # Print the date after the
        printDate(d)

        # In one row, all dates are on the same weekday but different week
        # Note that using "d = d + 7" instead of "d += 7" is because
        # former expression can make the program eazier to understand
        d = d + 7
    print("")

def calendar(m, y):
    # Important!!!
    # "daysSince1900(1, m, y)" calculates the number of days after 1-1-1900
    # We use daysSince1900(1, m, y) % 7. However, we need Monday to be 0 for correct alignment
    # Without adjusting by "(daysSince1900(1, m, y) - 1", Sunday is 7 and (7 % 7 == 0) which incorrectly moves Sunday to Monday
    # Finally, by multipling (-1) we can get the first day of the month (offset)
    d = ((daysSince1900(1, m, y) - 1) % 7) * (-1)

    weekday = 1
    # Using "weekday != 8" instead of "weekday <= 7" is because
    # the loop guard "weekday" is accurately 8 instead of "weekday > 7" which avoids ambiguity
    while weekday != 8:
        printRow(weekday, d, m, y)
        weekday = weekday + 1

# Start the program
prompt()
copyrightNotice()
input("Press Enter to exit. ")
exit(0)