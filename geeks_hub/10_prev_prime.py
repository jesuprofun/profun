# Given a number, find the prime number that comes first when we count backward.

def is_prime(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError
    
    if num <= 1:
        return False
        
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prev_prime(num):

    number = num - 1
    while True:
        ans = is_prime(number)
        if ans:
            return number
        else:
            number -= 1


number = int(input("Enter the number: "))

ans = prev_prime(number)
print("Previous prime number is: ", ans)