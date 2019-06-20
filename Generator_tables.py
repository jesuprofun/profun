
def tables(num):
    lyst = []
    for start in range(1, 11):
        ans = start * num
        # print(i, "*",  num, "=", ans)
        row = f"{start} * {num} = {ans}"
        lyst.append(row)
    return lyst
    

def tables_generator(num):
    final = tables(num)
    yield final


for i in range(1, 11):
    sq = tables_generator(i)
    print(next(sq))
    


