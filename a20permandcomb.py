


def findperm(numlist):

    perm = permutations(numlist)
    for i in list(perm):
        print(i)

def findcomb(numlist,n):
    comb = combinations(numlist,n)
    for i in list(comb):
        print(i)

from itertools import *
print("1.Permutations\n2.Combinations")
choice = int(input("Enter your choice:"))
if choice == 1:
    n = int(input("Enter the number for permutations: "))
    perm = []
    for i in range(n):
        num = int(input("Enter the numbers: "))
        perm.append(num)
    findperm(perm)
elif choice == 2:
    n = int(input("Enter the number for Combinations: "))
    comb = []
    for i in range(n):
        num = int(input("Enter the numbers: "))
        comb.append(num)
    findperm(comb,n)

