
l1 = ['Jesu ', 'Deva ', 'Caisey ', 'Chrisy ']
l2 = ['Profun ', 'Steffina ', 'Rona ', 'Riana ']
l3 = ['C.J', 'J', 'P', 'P']

l4 = list(map(lambda x, y, z : x + y + z, l1, l2, l3))
count = 0
for i in l4:
    count += 1
    print("Name {}".format(count),i)
