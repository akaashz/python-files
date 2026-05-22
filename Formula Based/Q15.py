#to find surface area and volume of a cylinder

r=float(input("Enter the radius of the cylinder:"))
h=float(input("Enter the height of the cylinder:"))

pi=3.14
surface_area=2*pi*r*(r+h)
volume=pi*r**2*h

print("Surface area of the cylinder: ",surface_area)
print("Volume of the cylinder: ",volume)