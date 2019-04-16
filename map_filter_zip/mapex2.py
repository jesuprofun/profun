# Write a map to calcuate area of the rectangles. The lists "length" and "breadh" contains length and breadh of rectangles

len_of_rect = [4, 6, 8, 10]
bredth_of_rect = [3, 5, 7, 9]

find_area = list(map(lambda l, b : l * b, len_of_rect, bredth_of_rect))
count = 0
for i in find_area:
    count += 1
    print("Area of rectangle No. {} is ".format(count), i)
