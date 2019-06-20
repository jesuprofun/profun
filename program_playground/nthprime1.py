
def is_prime(num):

    if not isinstance(num, int) or num <= 1:
        return False

    if num <= 3:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def next_prime(a, num):

    if not isinstance(num, int) or not isinstance(a, int):
        raise ValueError

    count = 0

    for i in range(a+1, 99999):
        if is_prime(i):
            count += 1
            if count == num:
                return i


n = next_prime(3, 4)
print(n)

