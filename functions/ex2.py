# Given the radius of the circle, write a function to return area and circumference
from math import pi
# find area of the circle
def area_of_circle(radius):
    return radius * radius

# find circumference of the circle
def circumference_of_circle(radius):
    return 2 * pi * radius

radius_of_circle = 10
area = area_of_circle(radius_of_circle)
circumference = circumference_of_circle(radius_of_circle)

print("area of the circle is ", area)
print("circumference of the circle", circumference)
