

netamount = 0
while True:
    cust_input = input("Enter D or W space amount for transcation: ")
    if not cust_input:
        break
    s = cust_input.split(' ')
    operation = s[0]
    amount = int(s[1])
    if operation == 'D':
        netamount += amount
    if operation == 'W':
        netamount -= amount
    else:
        pass
print("Available amount:",netamount)