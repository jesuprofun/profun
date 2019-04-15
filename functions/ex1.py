# Write a function that returns list of numbers from 0 to 1000 that are multiples of 3 and 7

def numbers():
    num_list = [x for x in range(0,1000) if x % 3 == 0 and x % 7 == 0]
    print(*num_list)

if __name__ == "__main__":
    numbers()
