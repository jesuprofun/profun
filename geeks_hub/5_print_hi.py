# Get the name of the user as inputs and greet the user saying 
# “Good Morning, " or "Good Afternoon, " depending upon the time of the day

from datetime import datetime

name = input("Enter your name: ")
date_time = datetime.now()

if date_time.hour < 12:
    print("Good Morning", name)
elif date_time.hour >= 12 or date_time.hour < 4:
    print("Good Afternoon", name)
else:
    print("Good Evening", name)