
password = input("Enter a valid password: ")
lyst = []
for i in password:
    if i.isalpha() or i.isdigit():
        lyst.append(i)
    else:
        print("wrong password")
print(''.join(lyst))
