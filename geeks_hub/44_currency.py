# Given the amount, write a program to find out the minimum number of coins/notes 
# required to total up to the amount. 
# For instance, denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1] 

lyst = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000] 

num = int(input("Enter the amount: "))
sum = 0
iteration = -2
count = 0
for d in lyst:
    iteration += 1
    if d < num:
        continue
    else:
        sum = sum + lyst[iteration]
        count += 1
        while sum < num:
            
            for i in range(iteration, 0, -1):
                sum = sum + lyst[i]
                count += 1
                if sum == num:
                    break
                elif sum > num:
                    sum = sum - lyst[i]
                    count -= 1
                elif sum < num:
                    sum = sum + 1
                    count += 1
                
        print(count)


        break
