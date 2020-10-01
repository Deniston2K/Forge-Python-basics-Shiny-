from math import sqrt

c1_x1=int(input("Enter the value of c1_x1:"))
c1_x2=int(input("Enter the value of c1_x2:"))
c2_y1=int(input("Enter the value of c2_y1:"))
c1_y2=int(input("Enter the value of c2_y2:"))

radius_1=int(input("Enter the radius of circle 1:"))
radius_2=int(input("Enter the radius of circle 2:"))

def sum_of_radius(radius_1,radius_2):
    total_radius=radius_1+radius_2
    return total_radius

def distance_between_centre(c1_x1,c1_x2,c2_y1,c1_y2):
    distance_between_centre=sqrt((c1_x2-c1_x1)**2-(c1_y2-c2_y1)**2)
    return distance_between_centre

sum=sum_of_radius(radius_1,radius_2)
distance=distance_between_centre(c1_x1,c1_x2,c2_y1,c1_y2)

if sum==distance:
    print("The two circles are touching")

elif sum<distance:
    print("The two circles are intersecting")

else:
    print("The two circles are separate")
