

numbers = [x for x in range(10)]
print(numbers)

numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x for x in range(10) if x % 2 == 0]
print(numbers)

numbers = ["Even" if x % 2 == 0 else "odd" for x in range(10)]
print(numbers)

alphabets = [x for x in 'MATHEMATICS' if x in ['A', 'E', 'I', 'O', 'U']]
print(alphabets)

numbers = [x for x in range(1,101) if int(x**0.5) == x**0.5]
print(numbers)
