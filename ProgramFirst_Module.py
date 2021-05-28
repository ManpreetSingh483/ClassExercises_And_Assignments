from math import pi


# Write a Python program which accepts the radius of a circle from the user and compute the area.radius
def calculate_circleArea():
    radius = float(input("Enter radius of circle: "))
    circleArea = pi * radius ** 2
    print(f'Area of cicle is : {circleArea:.2f}')




