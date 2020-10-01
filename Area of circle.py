from math import pi

def area(radius):
    area=pi*radius**2
    return area

radius=int(input("Enter the radius:"))
area=area(radius)
print("The area is:{}".format(area))