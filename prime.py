
def is_prime(num):
    if not isinstance(num, int):
        raise TypeError("Invalid Input")
    if num > 1:
        for i in range(2,num):
            if(num % i == 0):
                return False
        else:
            return True

    else:
        return False

if __name__ == '__main__':
    ans = is_prime(7)
    print(ans)