""" 
A program to Calculate The Areas of Triangle and Circle
Created by : Srayan Ray
"""

print("Welcome... Starting Calculator....")
option = raw_input("Enter the shape--'C' for Circle or 'T' for triangle: ")


def area_circle(radius):
	print("Radius of the Circle : "+str(radius))
	pi=3.14159
	area_of_circle = pi * radius ** 2
	print("The Area of the Circle of Radius "+str(radius) +"is: "+str(area_of_circle))

def area_triangle(height,base):
	print("The Altitude and Base of the triangle are : "+str(height) +" "+str(base))
	area_of_triangle = 0.5 * height * base
	print("The Area of the triangle is: "+str(area_of_triangle))

if option == "C":
	radius = float(input("Enter the Radius of the Cirlce >>  "))
	print("Calculating area....")
	area_circle(radius)
elif option == "T":
	height = float(input("Enter the Altitude of triangle >> "))
	base = float(input("Enter the base of the triangle >> "))
	print("Calculating Area....")
	area_triangle(height,base)
else:
	print("Wrong Choice! ... Enter the Correct choice...")

print(" Exiting Calculator....")