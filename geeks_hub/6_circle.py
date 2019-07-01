# Given the radius of the circle, write a program to print the circumference and 
# area of the circle. Write functions to calculate area and circumference

from math import pi
def area_circle(radius):
    return pi * radius ** 2

def circumference_circle(radius):
    return 2 * pi * radius


radius = float(input("Enter the radius of the circle: "))

area = area_circle(radius)
print("Area of the circle is:", area)

circumference = circumference_circle(radius)
print("circumference of the circle is:", circumference)