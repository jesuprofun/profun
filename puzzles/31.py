
def lyst(var, lyst_out = []):

    for i in range(var):
        lyst_out.append(i*i)
    return lyst_out


lyst1 = lyst(2)
lyst2 = lyst(1, [3, 2, 1])
lyst3 = lyst(3)


print(lyst1, lyst2,  lyst3)