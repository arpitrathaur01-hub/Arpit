# Question - Take diameter as input and calculate the area of a circle.

diameter= int(input("Enter the value of diameter :"))

radius = diameter/2

area= 3.14 * (radius ** 2)
print("Area of circle is" , area)
print("Radius of the circle is" , radius)