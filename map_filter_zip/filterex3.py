
lyst = ['pop', 'profun', 'dad','steffy']
res = filter(lambda x : x.lower() == x[::-1],lyst)
print(list(res))
