
students = [
    {
        "name": "profun",
        "Marks": 70
    },
    {
        "name": "steffy",
        "Marks": 80
    },
    {
        "name": "ria",
        "Marks": 90
    },
    {
        "name": "rona",
        "Marks": 95
    }
]
###################################################################
# using filter
x = list(filter(lambda student: student["Marks"] >= 80, students))

y = list(map(lambda student: student["Marks"], students))

print("Using filter function\n",x)
###################################################################
# using for loop
print("\n Using for loop")
for student in students:
    if student["Marks"] >= 80:
        print(student)
###################################################################
# Using List Comprehension

ans = [student for student in students if student["Marks"] >= 80]

print("\nUsing List Comprehension\n",(ans))

###################################################################