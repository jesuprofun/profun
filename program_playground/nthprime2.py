
"""Program to find nth prime number for the
given input a and number n"""

# to get the values for a & n
a = int(input("Enter the value for a: ")) # input() --> to get input from user
n = int(input("Enter the value for n: ")) # int(input()) --> to convert input value to integer

num = a*a
count = 0
for i in range(a+1, num):
    if num % i == 0:
        count += 1
        if count == n:
            print(i)
            break
