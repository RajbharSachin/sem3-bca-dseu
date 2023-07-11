import sys
n=len(sys.argv)
print("Total number of argument passed",n)
print("\nName of python Script",sys.argv[0])
print("\nArguement passed: ")
for i in range (1,n):
    print(sys.argv[i])  
sum=0
for i in range (1,n):
    sum+=int(sys.argv[i])
avg=sum/4 #total arguement is filename[at index 0] + other passed arguements
print("Average is ",avg)