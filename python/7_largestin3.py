a=int(input("Enter 1st number: "))
b=int(input("Enter 2st number: "))
c=int(input("Enter 3st number: "))
if(a>b):
    if(a>c):
        print(a," is greatest")
    else:
        print(c," is greatest")
else:
    if(b>c):
        print(b," is greatest")
    else:
        print(c," is greatest")