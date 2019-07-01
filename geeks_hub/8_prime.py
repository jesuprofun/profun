# Given a number, find whether or not it is prime

def is_prime(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError("Invalid Input")

    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True


num = int(input("Enter the number: "))

ans = is_prime(num)
if ans:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")