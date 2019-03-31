
import datetime
t = datetime.datetime.now()
print(t)
x = input("Enter your name:")
if t.hour <= 12:
    print("Goodmorning ", x)
else:
    print("Goodafternoon", x)