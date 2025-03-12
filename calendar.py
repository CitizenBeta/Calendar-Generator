# File Name: calendar.py
# Author: Zhang Anjun
# Date: 2025-03-12
# Description: A calendar generator
# Version: 1.0
# © 2025 Zhang Anjun. All rights reserved.

# Shared functions
def leap(y):
    if (((y%4 == 0) and (y%100 != 0)) or (y%400 == 0)):
        return True
    else:
        return False
    
def maxDays(m, y):
    if ((m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12)):
        return 31
    elif ((m == 4) or (m == 6) or (m == 9) or (m == 11)):
        return 30
    elif (m == 2):
        if leap(y):
            return 29
        else:
            return 28
        
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

def daysInFullMonthsBefore(m, y):
    total = 0
    i = 1
    while i != m:
        total = total + maxDays(i, y)
        i = i + 1
    return total

def daysSince1900(d, m, y):
    return daysInFullYearsBefore(y) + daysInFullMonthsBefore(m, y) + d

def whatDayWasIt(d, m, y):
    n = daysSince1900(d, m, y)
    if n % 7 == 1:
        return "Monday"
    elif n % 7 == 2:
        return "Tuesday"
    elif n % 7 == 3:
        return "Wednesday"
    elif n % 7 == 4:
        return "Thursday"
    elif n % 7 == 5:
        return "Friday"
    elif n % 7 == 6:
        return "Saturday"
    elif n % 7 == 0:
        return "Sunday"

# Calendar Generator
def prompt():
    m = int(input("Please enter a month: "))
    if not m >= 1 and m <= 12:
        print("Please enter a valid month")
        prompt()
    y = int(input("Please enter a year: "))
    if y < 1900:
        print("Please enter a valid month")
        prompt()
    print("")
    print("Calendar for", m, "-", y)
    calendar(m, y)

def row(week, d, m, y):
    if week == 1:
        print("Monday    |", end="")
    elif week == 2:
        print("Tuesday   |", end="")
    elif week == 3:
        print("Wednesday |", end="")
    elif week == 4:
        print("Thursday  |", end="")
    elif week == 5:
        print("Friday    |", end="")
    elif week == 6:
        print("Saturday  |", end="")
    elif week == 7:
        print("Sunday    |", end="")

    d = d + week
    while d <= maxDays(m, y):
        if d >= 10:
            print("  ", d, " ", end="", sep="")
        elif d < 10 and d > 0:
            print("   ", d, " ", end="", sep="")
        elif d <= 0:
            print("     ", end="", sep="")
        d = d + 7
    print("")

def calendar(m, y):
    whichDay = (daysSince1900(1, m, y)) % 7
    d = whichDay * (-1) + 1
    week = 1
    while week != 8:
        row(week, d, m, y)
        week = week + 1

prompt()
