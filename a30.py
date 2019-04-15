# Given a date, write a program to find the number of days between the given date and today

import datetime

# Get today's date
today_date = datetime.date.today()
print("Today's date is: ", today_date)


# Get date input from the user
get_date_time = input("Enter the date and time in the format YYYY-MM-DD: ")
date_time_strip = datetime.datetime.strptime(get_date_time, '%Y-%m-%d')
some_date = date_time_strip.date()

# Calculate the number of days
delta_date = some_date - today_date
print("{} is number of days between the given date and today".format(delta_date))
