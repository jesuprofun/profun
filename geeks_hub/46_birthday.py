# Birthday

import datetime

def get_input():
    name = input("Enter name: ")
    birthdate = input("Enter DOB in YYYY-MM-DD this format: ")
    year, month, date = map(int, birthdate.split('-'))
    dob = datetime.date(year, month, date)
    
    return name, dob

my_dict = {}
for i in range(3):

    name, dob = get_input()
    my_dict["name"] = dob
print(my_dict["profun"])

