
in_str = input("Enter a string: ")
d = {"Upper" : 0 , "Lower" : 0}
for i in in_str:
    if i.isupper():
        d["Upper"] += 1
    elif i.islower():
        d["Lower"] += 1
    else:
        pass
print("Upper = ", d["Upper"])
print("Lower = ", d["Lower"])
