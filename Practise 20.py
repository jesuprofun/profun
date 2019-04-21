
def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return False
        else:
            return True

lyst = [x for x in range(0,40)]
res = list(filter(is_prime, lyst))
print(res)