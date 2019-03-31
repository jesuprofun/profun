
def ascending(total,count):
    for i in range(count):
        for j in range(i + 1, count):
            if total[i] > total[j]:
                temp = total[i]
                total[i] = total[j]
                total[j] = temp
    return total
