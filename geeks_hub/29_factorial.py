# Write a program to find the factorial of the given number

def fact(num): 
    ans = 1
    for i in range(num, 0, -1):
        ans = ans * i
    return ans

def fact_rec(num):

    if num == 0:
        return 1
    else:
        return num * fact_rec(num-1) 



n = int(input("Enter the number for factorial: "))
print("Factorial of {} in normal method is {}".format(n, fact(n)))

print("Factorial of {} in recursion method is {}".format(n, fact_rec(n)))
