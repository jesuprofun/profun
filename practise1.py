#
# def func(x, y, z):
#     return x + y + z
#
# x = [1, 2, 3, 4]
# y = [10, 20, 30, 40]
# z = [6, 7, 8, 9]
# a = [2,3,4]
# result = list(map(func, x, y, z, a))
#
# print(result)
#
# for i in result:
#     print(i)


# l1 = [1,2,3,4,5,6]
# l2 = [7,8,9,10]
# l3 = [2,3,4,2,3]
#
# res_list = map(lambda a,b,c:a+b+c, l1, l2,l3)
#
# print(list(res_list))



# l1 = [1,2,3]
# l2 = [10,20,30]
#
# res = zip(l1,l2)
#
#
# print(list(res))

#
# li = [i**2 for i in range(10)]
# print(li)

# mul = [x for x in range(0,100) if x%3 == 0]
# print(mul)
#
# l1 = [x for x in range(100)]
# res_list = filter(lambda x:x%3==0, l1)
# print(list(res_list))
#
# def mul(x):
#     return x%3 == 0
#
# third_list = filter(mul, l1)
# print(list(third_list))


# i = 13
# prime = [x for x in range(2,100) if i%x == 0]
# print(prime)

# l1 = [x for x in range(100)]
# res_list = filter(lambda x:x%3==0, l1)
# print(list(res_list))
#
# def is_prime(x):
#     for i in range(2,x):
#         return  x%i == 0
#
# l3 = [x for x in range(100)]
# print(l3)
# third_list = filter(is_prime, l3)
# print(list(third_list))

result  = [x for x in range(20) if x%2==0 False]
print(result)
