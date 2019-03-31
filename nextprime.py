

def nextprime(a,b):
    for num in range(a,b):
        for i in range(2,num):
            if(num % i == 0):
                break
        else:
            print(num,end=" ")
            break




n = int(input("Enter the number"))
nextprime(n+1,n*n)



