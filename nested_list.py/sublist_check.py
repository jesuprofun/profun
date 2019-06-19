
def check(lyst1, lyst2):
    for sublist1 in lyst1:
        for sublist2 in lyst2:
            if sublist1 == sublist2:
                return True
    else:
        return False

lyst1 = [[2, 3, 1], [4, 5], [6, 8]]
lyst2 = [[4, 5, 3], [6, 8, 4]]

print(check(lyst1, lyst2))