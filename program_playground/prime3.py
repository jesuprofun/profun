
""" To find whether the given number is prime or not
    a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)."""

# Getting the input from user
# input() --> gets the input
# int(input) --> converts the input to integer 
num = int(input("Enter the number: "))

# If the number less than or equal to 1 --> It is not a Prime number
if num <= 1:
    print("Not Prime")


for i in range(2, num):
    if num % i == 0:
        print("Not Prime Number")
        break

else:
    print("Prime")


