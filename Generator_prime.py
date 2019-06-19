

def is_prime(num):

    if not isinstance(num, int) or num <= 1:
        raise ValueError

    if num <= 3:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True


def next_prime(num):

    number = num + 1

    while True:
        if is_prime(number):
            yield number
    
        number += 1


x = next_prime(8)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

for i in range(10):
    print(next(x))
    