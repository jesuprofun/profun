
def compound_interest(p = 1000, n = 2, r = 0.07):
    ci = p * (1 + (r / 100)) ** n
    return ci

# by passing arguments
ci = compound_interest(1200, 2, 5.4)
print("Compound interest is ", ci)

# takes the default values
ci2 = compound_interest()
print("Compound interest by default ", ci2)

# by passing named arguments
ci3 = compound_interest(p = 2000, n =3, r = 1)
print("Compound interest by passing named arguments ", ci3)

#  passing named arguments in out of order
ci3 = compound_interest(r = 1, n =3, p = 2000)
print("Compound interest by passing named arguments in out of order ", ci3)
