#implicit_typecast
x=123
y=20.35
z=x+y
print("Data Type of Z is ",type(z))

#explicit_typecast
a=123
b="456"
print("Data type of a is ",type(a))
print("Data type of b is ",type(b))
b=int(b)
print("data type of b is ",type(b))
c=a+b
print("Data type of c is ",type(c))