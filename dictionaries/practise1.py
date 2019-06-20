
def sum(lyst, num):

    length = len(lyst)
    if num < lyst[0] or num > lyst[length-1]:
        return False

    total = lyst[0] + lyst[length-1]
    for i in range(length):
        if total > num:
            total = lyst[0] + lyst[]



lyst = [1, 2, 3, 4, 5, 6, 7, 8]

num = 8

ans = sum(lyst, num)
print(ans)