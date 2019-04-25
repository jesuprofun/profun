import re

a = r"Cookie"
b = "Cookie"
if re.match(a, b):
    print("Match")
else:
    print("Mot a match")