# program to find largest of three numbers using function max_of_three() 
def max_of_three(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    else: 
        return n3
# driver code
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
print("\nLargest among three nos:- ",max_of_three(n1,n2,n3))