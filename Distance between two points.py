from math import sqrt

x1=int(input("Enter the value of x1:"))
x2=int(input("Enter the value of x2:"))
y1=int(input("Enter the value of y1:"))
y2=int(input("Enter the value of y2:"))

def distance(x1,x2,y1,y2):
    distance=sqrt((x2-x1)**2-(y2-y1)**2)
    return distance
distance=distance(x1,x2,y1,y2)
print("The distance is:{}".format(distance))
