# normal function
def add(n):
    return n+4
print(add(4))

# lambda function
add=lambda n:n+4
print(add(4))
 
# with filter
l=[13,20,17,40,80]
even=list(filter(lambda x:x%2==0,l))
print(even)

# with map
n=[2,4,5,10]
s=list(map(lambda x:x*10,n))
print(s)

# Reduce function
import functools
n=[1,3,5,6,2]
print(functools.reduce(lambda a,b: a+b,n)) # sum of all list items.
print(functools.reduce(lambda a,b: a if a>b else b,n)) # find greatest of all list items.

# Nested function
def f1():
    s=10
    def f2():
        print(s)
    f2()
f1()

# Recursion
def fact(n):
    if(n==1)or(n==0):
        return 1
    else:
        return (n*fact(n-1))

n=5
print("Factorial is ",fact(n))