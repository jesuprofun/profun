
#i = 1
#a = 1
#while i < 100:
 #   if ((a % 3 and a % 5) == 0):
  #      a += 1

   # else:
    #    print(a)
     #   a += 1
    #i += 1


for i in range(1,100):
    if i%3==0 or i%5==0:
        continue
    print(i,end=' ')

print()