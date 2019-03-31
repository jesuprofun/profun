


def preprime(a,b):
    for num in range(a,b,-1):
        for i in range(2,num):
            if(num % i == 0):
                break
        else:
            print(num,end=" ")
            break




n = int(input("Enter the number"))
preprime(n-1,2)



