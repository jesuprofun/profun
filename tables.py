
def tables(num,r):
    for i in range(1,r):
        ans = num * i
        print(num ,"*" ,i ,"=" ,ans)

num = int(input("Enter the Number for table"))
r = int(input("Enter the number for range"))
tables(num,r)
