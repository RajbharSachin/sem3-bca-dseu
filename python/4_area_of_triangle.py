a=int(input("Enter first side"))
b=int(input("Enter second side"))
c=int(input("Enter third side"))
s=(a+b+c)/2
area_of_t=((s*(s-a)*(s-b)*(s-c))**(1/2))
print("Area of triangle: ",area_of_t)
