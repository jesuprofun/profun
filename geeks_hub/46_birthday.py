# Birthday

import datetime

def get_input():
    name = input("Enter name: ")
    birthdate = input("Enter DOB in YYYY-MM-DD this format: ")
    year, month, date = map(int, birthdate.split('-'))
    dob = datetime.date(year, month, date)

    return name, dob


def by_name():
    name_dict = {}
    date_dict = {}

    for i in range(2):

        name, dob = get_input()
        name_dict[name] = dob
        date_dict[dob] = name

    
    find_name = input("Enter name of your choice: ")
    # print(find_name in name_dict)
    print(name_dict[find_name])
    # print(date_dict[1989-08-25])


by_name()