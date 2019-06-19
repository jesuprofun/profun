

def next_prime(a, b):

    for num in range(a, b):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
            break


n = int(input("Enter the number"))
next_prime(n+1, n*n)



