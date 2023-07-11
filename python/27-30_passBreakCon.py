# A break statement, when used inside the loop, will terminate the loop and exit. If used inside nested loops, it will break out from the current loop.
# A continue statement, when used inside a loop, will stop the current execution, and the control will go back to the start of the loop.
# Python pass is a null statement,  it does nothing and is ignored.
# A return statement is used to end the execution of the function call and “returns” the result 


my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'] 
# break in for-loop
for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'Guru':
        print('Found the name Guru')
        break
        print('After break statement')
print('Loop is Terminated')
# break in while-loop
i = 0
while True:
    print(my_list[i])
    if (my_list[i] == 'Guru'):
        print('Found the name Guru')
        break
        print('After break statement')
    i += 1
print('After while-loop exit')

# Continue inside for-loop
for i in range(10):    
    if i == 7:
        continue  
    print("The Number is :" , i)
# Continue inside while-loop
i = 0
while i <= 10:    
    if i == 7:
        i += 1
        continue  
    print("The Number is  :" , i)
    i += 1

# Pass statement in for-loop
test = "Guru"
for i in test: 
    if i == 'r': 
        print('Pass executed') 
        pass
    print(i)

# python return statements

# A Python program to return multiple 
# values from a method using tuple
# This function returns a tuple
def fun():
    str = "geeksforgeeks"
    x = 20
    return str, x;  # Return tuple, we could also
                    # write (str, x) 
# Driver code to test above method
str, x = fun() # Assign returned tuple
print(str)
print(x)

# A Python program to return multiple 
# values from a method using list
# This function returns a list
def fun():
    str = "geeksforgeeks"
    x = 20  
    return [str, x];   
# Driver code to test above method
list = fun() 
print(list)

# A Python program to return multiple 
# values from a method using dictionary
# This function returns a dictionary
def fun():
    d = dict(); 
    d['str'] = "GeeksforGeeks"
    d['x']   = 20
    return d  
# Driver code to test above method
d = fun() 
print(d)

# Python program to illustrate functions
# can return another function
def create_adder(x):
    def adder(y):
        return x + y
    return adder
add_15 = create_adder(15)
print("The result is", add_15(10))
 
# Returning different function
def outer(x):
    return x * 10
def my_func():    
    # returning different function
    return outer 
# storing the function in res
res = my_func()
print("\nThe result is:", res(10))