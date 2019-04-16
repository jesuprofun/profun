
# area
def area(a,b):
    if b == None:
        return a * a
    else:
        return a * b

choice = int(input("1. Area of the Square\n2. Area of the rectangle\nEnter your choice"))

if choice == 1:
    side_of_square = int(input("Enter the side of the square: "))
    square = area(side_of_square, None)
    print("area of the square is", square)
elif choice == 2:
    len_of_rect = int(input("Enter the length of the rectangle: "))
    bread_of_rect = int(input("Enter the breadth of the rectangle: "))
    rect = area(len_of_rect,bread_of_rect)
    print("area of the rectangle is", rect)
