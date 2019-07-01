# Write a program which will find all such numbers which are 
# divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included)

def divisible(start, end):
    for num in range(start, end+1):
        if (num % 7 == 0):
            if num % 5 == 0:
                pass
            else:
                print(num)

    
divisible(2000, 3200)
