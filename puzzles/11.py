

in_str = input("Enter a string: ")
d = {"digits" : 0 , "Alpha" : 0}
for i in in_str:
    if i.isdigit():
        d["digits"] += 1
    elif i.isalpha():
        d["Alpha"] += 1
    else:
        pass

print("Digits = ",d["digits"])
print("Alpha = ",d["Alpha"])
