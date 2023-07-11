# program to find type of triangle
print("Input lengths of the triangle sides:- ")
s1 = int(input("1st side: "))
s2 = int(input("2nd side: "))
s3 = int(input("3rd side: "))

if (s1==s2==s3) :
    print("\nEquilateral triangle")
elif (s1==s2 or s2==s3 or s1==s3) :
    print("\nIsosceles triangle")
else :
    print("\nScalene triangle")