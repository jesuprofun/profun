
def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

lyst = [x for x in range(1000)]
res = filter(is_prime, lyst)
print(list(res))
