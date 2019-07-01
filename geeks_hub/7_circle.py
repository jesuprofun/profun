# Given the area of the circle, write a program to print the radius

from math import sqrt, pi

def find_area(area):
    return sqrt(area / pi)


area = float(input("Enter the area of the circle:"))

radius = find_area(area)
print("Radius of the circle is", radius)