# Use try/except for more than one line exceptions (it's fast)
try:
    sum = 0 
    print("Enter 20 positive numbers:-\n")
    for i in range(1,21):
        choice = int(input())
        sum = sum + choice
        assert choice >= 0 # Test if it true
    print("Average is ",sum/20)
except AssertionError :
    print("Number is negative")

                            # OR
sum = 0 
#create an empty list
myList=[]
print("Enter 20 positive numbers:-\n")
for i in range(0,20):
    myList.append(int(input()))  
    if myList[i] < 0:
        myError = ValueError('All values should be a positive number')
        raise myError
    sum = sum + myList[i]
    
print("Average is ",sum/20)
