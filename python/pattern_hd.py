for i in range(4):
        print('*' * (i+1))
#or

def print_pyramid(size):
    for row in range(0, size):
        for col in range(0, row+1):
            print("*", end=" ")
        print("")
size = int(input("Enter the size of the Pyramid : "))
print_pyramid(size)

n = int(input("Enter the number of rows for pyramid:"))
k = n-1
for i in range(0, n,2):
    for j in range(0, k):
        print(end=" ") 
    k = k - 2
    for j in range(0, i+1):
        print("* ",end='')
    print("")