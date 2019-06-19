
# n = int(input("Enter the number: "))
# a = n+1
# b = n*n

# for num in range(a, b):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)
#         break

a = int(input("Enter the number: "))
b = a+1
count = 1

while count > 0:
    for i in range(2, b):
        if b % i == 0:
            b += 1
        else:
            count -= 1

print(b)