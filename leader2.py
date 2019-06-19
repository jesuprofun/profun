
def leader(lyst):

    leader = lyst[-1]
    print(leader)
    for i in range(len(lyst)-1, 0, -1):
        
        if lyst[i] > leader:
            leader = lyst[i]
            print(leader)


lyst = [16, 17, 4, 3, 5, 2]

leader(lyst)

# for i in range(10, 0, -2):
#     print(i)