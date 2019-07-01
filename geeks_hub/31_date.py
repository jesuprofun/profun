# Given a date, write a program to find the number of days between the given date and today

import datetime

def today_date():

    today = datetime.date.today()
    return today

def given_date():

    date_format = input("Enter date in YYYY-MM-DD format: ")
    year, month, day = map(int, date_format.split('-'))
    given = datetime.date(year, month, day)
    
    return given

present = today_date()
given = given_date()

difference = present - given
print(difference)